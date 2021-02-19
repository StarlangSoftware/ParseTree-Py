from __future__ import annotations

from Dictionary.Word import Word

from ParseTree.ConstituentSpan import ConstituentSpan
from ParseTree.SearchDirectionType import SearchDirectionType
from ParseTree.Symbol import Symbol


class ParseNode:
    children: list
    parent: ParseNode
    data: Symbol

    ADJP = ["NNS", "QP", "NN", "$", "ADVP", "JJ", "VBN", "VBG", "ADJP", "JJR", "NP", "JJS", "DT", "FW", "RBR", "RBS",
            "SBAR", "RB"]
    ADVP = ["RB", "RBR", "RBS", "FW", "ADVP", "TO", "CD", "JJR", "JJ", "IN", "NP", "JJS", "NN"]
    CONJP = ["CC", "RB", "IN"]
    FRAG = []
    INTJ = []
    LST = ["LS", ":"]
    NAC = ["NN", "NNS", "NNP", "NNPS", "NP", "NAC", "EX", "$", "CD", "QP", "PRP", "VBG", "JJ", "JJS", "JJR", "ADJP",
           "FW"]
    PP = ["IN", "TO", "VBG", "VBN", "RP", "FW"]
    PRN = []
    PRT = ["RP"]
    QP = ["$", "IN", "NNS", "NN", "JJ", "RB", "DT", "CD", "NCD", "QP", "JJR", "JJS"]
    RRC = ["VP", "NP", "ADVP", "ADJP", "PP"]
    S = ["TO", "IN", "VP", "S", "SBAR", "ADJP", "UCP", "NP"]
    SBAR = ["WHNP", "WHPP", "WHADVP", "WHADJP", "IN", "DT", "S", "SQ", "SINV", "SBAR", "FRAG"]
    SBARQ = ["SQ", "S", "SINV", "SBARQ", "FRAG"]
    SINV = ["VBZ", "VBD", "VBP", "VB", "MD", "VP", "S", "SINV", "ADJP", "NP"]
    SQ = ["VBZ", "VBD", "VBP", "VB", "MD", "VP", "SQ"]
    UCP = []
    VP = ["TO", "VBD", "VBN", "MD", "VBZ", "VB", "VBG", "VBP", "VP", "ADJP", "NN", "NNS", "NP"]
    WHADJP = ["CC", "WRB", "JJ", "ADJP"]
    WHADVP = ["CC", "WRB"]
    WHNP = ["WDT", "WP", "WP$", "WHADJP", "WHPP", "WHNP"]
    WHPP = ["IN", "TO", "FW"]
    NP1 = ["NN", "NNP", "NNPS", "NNS", "NX", "POS", "JJR"]
    NP2 = ["NP"]
    NP3 = ["$", "ADJP", "PRN"]
    NP4 = ["CD"]
    NP5 = ["JJ", "JJS", "RB", "QP"]

    def __init__(self, dataOrParent, leftOrLine=None, rightOrIsLeaf=None):
        """
        Another simple constructor for ParseNode. It takes inputs left and right children of this node, and the data.
        Sets the corresponding attributes with these inputs.

        PARAMETERS
        ----------
        dataOrParent
            Data for this node.
        leftOrLine
            Left child of this node.
        rightOrIsLeaf
            Right child of this node.
        """
        self.children = []
        self.parent = None
        self.data = None
        if isinstance(dataOrParent, Symbol) and isinstance(leftOrLine, ParseNode) and isinstance(rightOrIsLeaf,
                                                                                                 ParseNode):
            self.data = dataOrParent
            if rightOrIsLeaf is not None:
                self.children.append(leftOrLine)
                leftOrLine.parent = self
                self.children.append(rightOrIsLeaf)
                rightOrIsLeaf.parent = self
            else:
                if leftOrLine is not None:
                    self.children.append(leftOrLine)
                    leftOrLine.parent = self
        elif (isinstance(dataOrParent, ParseNode) or dataOrParent is None) and isinstance(leftOrLine, str) and isinstance(rightOrIsLeaf, bool):
            parenthesisCount = 0
            childLine = ""
            self.parent = dataOrParent
            if rightOrIsLeaf:
                self.data = Symbol(leftOrLine)
            else:
                self.data = Symbol(leftOrLine[1: leftOrLine.index(" ")])
                if leftOrLine.index(")") == leftOrLine.rindex(")"):
                    self.children.append(ParseNode(self, leftOrLine[leftOrLine.index(" ") + 1: leftOrLine.index(")")],
                                                   True))
                else:
                    for i in range(leftOrLine.index(" ") + 1, len(leftOrLine)):
                        if leftOrLine[i] != " " or parenthesisCount > 0:
                            childLine = childLine + leftOrLine[i]
                        if leftOrLine[i] == "(":
                            parenthesisCount = parenthesisCount + 1
                        elif leftOrLine[i] == ")":
                            parenthesisCount = parenthesisCount - 1
                        if parenthesisCount == 0 and len(childLine) != 0:
                            self.children.append(ParseNode(self, childLine.strip(), False))
                            childLine = ""

    def __searchHeadChild(self, priorityList: list, direction: SearchDirectionType, defaultCase: bool) -> ParseNode:
        """
        Extracts the head of the children of this current node.

        PARAMETERS
        ----------
        priorityList : list
            Depending on the pos of current node, the priorities among the children are given with this parameter
        direction : SearchDirectionType
            Depending on the pos of the current node, search direction is either from left to right, or from right to
            left.
        defaultCase : bool
            If true, and no child appears in the priority list, returns first child on the left, or first child on the
            right depending on the search direction.

        RETURNS
        -------
        ParseNode
            Head node of the children of the current node
        """
        if direction == SearchDirectionType.LEFT:
            for item in priorityList:
                for child in self.children:
                    if child.getData().trimSymbol().getName() == item:
                        return child
            if defaultCase:
                return self.firstChild()
        elif direction == SearchDirectionType.RIGHT:
            for item in priorityList:
                for j in range(len(self.children), -1, -1):
                    child = self.children[j]
                    if child.getData().trimSymbol().getName() == item:
                        return child
            if defaultCase:
                return self.lastChild()
        return None

    def headLeaf(self) -> ParseNode:
        """
        If current node is not a leaf, it has one or more children, this method determines recursively the head of
        that (those) child(ren). Otherwise, it returns itself. In this way, this method returns the head of all leaf
        successors.

        RETURNS
        -------
        ParseNode
            Head node of the descendant leaves of this current node.
        """
        if len(self.children) > 0:
            head = self.headChild()
            if head is not None:
                return head.headLeaf()
            else:
                return None
        else:
            return self

    def headChild(self) -> ParseNode:
        """
        Calls searchHeadChild to determine the head node of all children of this current node. The search direction and
        the search priority list is determined according to the symbol in this current parent node.

        RETURNS
        -------
        ParseNode
            Head node among its children of this current node.
        """
        if self.data.trimSymbol().__str__() == "ADJP":
            return self.__searchHeadChild(self.ADJP, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "ADVP":
            return self.__searchHeadChild(self.ADVP, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "CONJP":
            return self.__searchHeadChild(self.CONJP, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "FRAG":
            return self.__searchHeadChild(self.FRAG, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "INTJ":
            return self.__searchHeadChild(self.INTJ, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "LST":
            return self.__searchHeadChild(self.LST, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "NAC":
            return self.__searchHeadChild(self.NAC, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "PP":
            return self.__searchHeadChild(self.PP, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "PRN":
            return self.__searchHeadChild(self.PRN, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "PRT":
            return self.__searchHeadChild(self.PRT, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "QP":
            return self.__searchHeadChild(self.QP, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "RRC":
            return self.__searchHeadChild(self.RRC, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "S":
            return self.__searchHeadChild(self.S, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "SBAR":
            return self.__searchHeadChild(self.SBAR, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "SBARQ":
            return self.__searchHeadChild(self.SBARQ, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "SINV":
            return self.__searchHeadChild(self.SINV, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "SQ":
            return self.__searchHeadChild(self.SQ, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "UCP":
            return self.__searchHeadChild(self.UCP, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "VP":
            return self.__searchHeadChild(self.VP, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "WHADJP":
            return self.__searchHeadChild(self.WHADJP, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "WHADVP":
            return self.__searchHeadChild(self.WHADVP, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "WHNP":
            return self.__searchHeadChild(self.WHNP, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "WHPP":
            return self.__searchHeadChild(self.WHPP, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "NP":
            if self.lastChild().getData().getName() == "POS":
                return self.lastChild()
            else:
                result = self.__searchHeadChild(self.NP1, SearchDirectionType.RIGHT, False)
                if result is not None:
                    return result
                else:
                    result = self.__searchHeadChild(self.NP2, SearchDirectionType.LEFT, False)
                    if result is not None:
                        return result
                    else:
                        result = self.__searchHeadChild(self.NP3, SearchDirectionType.RIGHT, False)
                        if result is not None:
                            return result
                        else:
                            result = self.__searchHeadChild(self.NP4, SearchDirectionType.RIGHT, False)
                            if result is not None:
                                return result
                            else:
                                result = self.__searchHeadChild(self.NP5, SearchDirectionType.RIGHT, False)
                                if result is not None:
                                    return result
                                else:
                                    return self.lastChild()
        return None

    def addChild(self, child: ParseNode, index=None):
        """
        Adds a child node at the end of the children node list.

        PARAMETERS
        ----------
        child : ParseNode
            Child node to be added.
        index
            Position to be added.
        """
        if index is None:
            self.children.append(child)
        else:
            self.children.insert(index, child)
        child.parent = self

    def correctParents(self):
        """
        Recursive method to restore the parents of all nodes below this node in the hierarchy.
        """
        for child in self.children:
            child.parent = self
            child.correctParents()

    def removeXNodes(self):
        """
        Recursive method to remove all nodes starting with the symbol X. If the node is removed, its children are
        connected to the next sibling of the deleted node.
        """
        i = 0
        while i < len(self.children):
            if self.children[i].getData().getName().startswith("X"):
                self.children.insert(i + 1, self.children[i].children)
                self.children.pop(i)
            else:
                i = i + 1
        for child in self.children:
            child.removeXNodes()

    def setChild(self, index: int, child: ParseNode):
        """
        Replaces a child node at the given specific with a new child node.

        PARAMETERS
        ----------
        index : int
            Index where the new child node replaces the old one.
        child : ParseNode
            Child node to be replaced.
        """
        self.children[index] = child

    def removeChild(self, child: ParseNode):
        """
        Removes a given child from children node list.

        PARAMETERS
        ----------
        child : ParseNode
            Child node to be deleted.
        """
        self.children.remove(child)

    def leafCount(self) -> int:
        """
        Recursive method to calculate the number of all leaf nodes in the subtree rooted with this current node.

        RETURNS
        -------
        int
            Number of all leaf nodes in the current subtree.
        """
        if len(self.children) == 0:
            return 1
        else:
            total = 0
            for child in self.children:
                total += child.leafCount()
            return total

    def nodeCount(self) -> int:
        """
        Recursive method to calculate the number of all nodes in the subtree rooted with this current node.

        RETURNS
        -------
        int
            Number of all nodes in the current subtree.
        """
        if len(self.children) > 0:
            total = 1
            for child in self.children:
                total += child.nodeCount()
            return total
        else:
            return 1

    def nodeCountWithMultipleChildren(self) -> int:
        """
        Recursive method to calculate the number of all nodes, which have more than one children, in the subtree rooted
        with this current node.

        RETURNS
        -------
        int
            Number of all nodes, which have more than one children, in the current subtree.
        """
        if len(self.children) > 1:
            total = 1
            for child in self.children:
                total += child.nodeCountWithMultipleChildren()
            return total
        else:
            return 0

    def numberOfChildren(self) -> int:
        """
        Returns number of children of this node.

        RETURNS
        -------
        int
            Number of children of this node.
        """
        return len(self.children)

    def getChild(self, i: int) -> ParseNode:
        """
        Returns the i'th child of this node.

        PARAMETERS
        ----------
        i : int
            Index of the retrieved node.

        RETURNS
        -------
        ParseNode
            i'th child of this node.
        """
        return self.children[i]

    def firstChild(self) -> ParseNode:
        """
        Returns the first child of this node.

        RETURNS
        -------
        ParseNode
            First child of this node.
        """
        return self.children[0]

    def lastChild(self) -> ParseNode:
        """
        Returns the last child of this node.

        RETURNS
        -------
        ParseNode
            Last child of this node.
        """
        return self.children[len(self.children) - 1]

    def isLastChild(self, child: ParseNode) -> bool:
        """
        Checks if the given node is the last child of this node.

        PARAMETERS
        ----------
        child : ParseNode
            To be checked node.

        RETURNS
        -------
        bool
            True, if child is the last child of this node, false otherwise.
        """
        return self.children[len(self.children) - 1] == child

    def getChildIndex(self, child: ParseNode) -> int:
        """
        Returns the index of the given child of this node.

        RETURNS
        -------
        int
            Index of the child of this node.
        """
        return self.children.index(child)

    def isDescendant(self, node: ParseNode) -> bool:
        """
        Returns true if the given node is a descendant of this node.

        RETURNS
        -------
        bool
            True if the given node is descendant of this node.
        """
        for child in self.children:
            if child == node:
                return True
            elif child.isDescendant(node):
                return True
        return False

    def previousSibling(self) -> ParseNode:
        """
        Returns the previous sibling (sister) of this node.

        RETURNS
        -------
        ParseNode
            If this is the first child of its parent, returns null. Otherwise, returns the previous sibling of this
            node.
        """
        for i in range(1, len(self.parent.children)):
            if self.parent.children[i] == self:
                return self.parent.children[i - 1]
        return None

    def nextSibling(self) -> ParseNode:
        """
        Returns the next sibling (sister) of this node.

        RETURNS
        -------
        ParseNode
            If this is the last child of its parent, returns null. Otherwise, returns the next sibling of this node.
        """
        for i in range(0, len(self.parent.children) - 1):
            if self.parent.children[i] == self:
                return self.parent.children[i + 1]
        return None

    def getParent(self) -> ParseNode:
        """
        Accessor for the parent attribute.

        RETURNS
        -------
        ParseNode
            Parent of this node.
        """
        return self.parent

    def getData(self) -> Symbol:
        """
        Accessor for the data attribute.

        RETURNS
        -------
        Symbol
            Data of this node.
        """
        return self.data

    def setData(self, data: Symbol):
        """
        Mutator of the data attribute.

        PARAMETERS
        ----------
        data : Symbol
            Data to be set.
        """
        self.data = data

    def wordCount(self, excludeStopWords: bool) -> int:
        """
        Recursive function to count the number of words in the subtree rooted at this node.

        PARAMETERS
        ----------
        excludeStopWords : bool
            If true, stop words are not counted.

        RETURNS
        -------
        int
            Number of words in the subtree rooted at this node.
        """
        if len(self.children) == 0:
            if not excludeStopWords:
                total = 1
            else:
                if Word.isPunctuationSymbol(self.data.getName()) or \
                        "*" in self.data.getName().lower() or self.data.getName().lower() == "at" or self.data.getName().lower() == "the" or \
                        self.data.getName().lower() == "to" or self.data.getName().lower() == "a" or self.data.getName().lower() == "an" or \
                        self.data.getName().lower() == "not" or self.data.getName().lower() == "is" or self.data.getName().lower() == "was" or \
                        self.data.getName().lower() == "were" or self.data.getName().lower() == "have" or \
                        self.data.getName().lower() == "had" or self.data.getName().lower() == "has" or \
                        self.data.getName().lower() == "by" or self.data.getName().lower() == "at" or self.data.getName().lower() == "'re" or \
                        self.data.getName().lower() == "on" or self.data.getName().lower() == "off" or self.data.getName().lower() == "'s" or \
                        self.data.getName().lower() == "n't" or self.data.getName().lower() == "can" or \
                        self.data.getName().lower() == "could" or self.data.getName().lower() == "may" or \
                        self.data.getName().lower() == "might" or self.data.getName().lower() == "will" or \
                        self.data.getName().lower() == "would" or self.data.getName().lower() == "as" or\
                        self.data.getName().lower() == "with" or self.data.getName().lower() == "for" or self.data.getName().lower() == "in" or\
                        self.data.getName().lower() == "will" or self.data.getName().lower() == "would" or \
                        self.data.getName().lower() == "than" or self.data.getName().lower() == "$" or \
                        self.data.getName().lower() == "and" or self.data.getName().lower() == "or" or self.data.getName().lower() == "of" or \
                        self.data.getName().lower() == "are" or self.data.getName().lower() == "be" or \
                        self.data.getName().lower() == "been" or self.data.getName().lower() == "do" or self.data.getName().lower() == "few" or\
                        self.data.getName().lower() == "there" or self.data.getName().lower() == "up" or self.data.getName().lower() == "down":
                    total = 0
                else:
                    total = 1
        else:
            total = 0
        for child in self.children:
            total += child.wordCount(excludeStopWords)
        return total

    def isLeaf(self) -> bool:
        """
        Returns True if this node is leaf, False otherwise.

        RETURNS
        -------
        bool
            True if this node is leaf, False otherwise.
        """
        return len(self.children) == 0

    def isDummyNode(self) -> bool:
        """
        Returns True if this node does not contain a meaningful data, False otherwise.

        RETURNS
        -------
        bool
            True if this node does not contain a meaningful data, False otherwise.
        """
        return "*" in self.getData().getName() or (self.getData().getName() == "0" and
                                                   self.parent.getData().getName() == "-NONE-")

    def __str__(self) -> str:
        """
        Recursive function to convert the subtree rooted at this node to a string.

        RETURNS
        -------
        str
            A string which contains all words in the subtree rooted at this node.
        """
        if len(self.children) < 2:
            if len(self.children) < 1:
                return self.getData().getName()
            else:
                return "(" + self.data.getName() + " " + self.firstChild().__str__() + ")"
        else:
            st = "(" + self.data.getName()
            for child in self.children:
                st += " " + child.__str__()
            return st + ") "

    def moveLeft(self, node: ParseNode):
        """
        Swaps the given child node of this node with the previous sibling of that given node. If the given node is the
        leftmost child, it swaps with the last node.

        PARAMETERS
        ----------
        node : ParseNode
            Node to be swapped.
        """
        for i in range(len(self.children)):
            if self.children[i] == node:
                if i == 0:
                    self.children[0], self.children[len(self.children) - 1] = \
                        self.children[len(self.children) - 1], self.children[0]
                else:
                    self.children[i], self.children[(i - 1) % len(self.children)] = \
                        self.children[(i - 1) % len(self.children)], self.children[i]
                return
        for child in self.children:
            child.moveLeft(node)

    def moveRight(self, node: ParseNode):
        """
        Swaps the given child node of this node with the next sibling of that given node. If the given node is the
        rightmost child, it swaps with the first node.

        PARAMETERS
        ----------
        node : ParseNode
            Node to be swapped.
        """
        for i in range(len(self.children)):
            if self.children[i] == node:
                self.children[i], self.children[(i + 1) % len(self.children)] = \
                    self.children[(i + 1) % len(self.children)], self.children[i]
                return
        for child in self.children:
            child.moveRight(node)

    def ancestorString(self) -> str:
        """
        Recursive function to concatenate the data of the all ascendant nodes of this node to a string.

        RETURNS
        -------
        str
            A string which contains all data of all the ascendant nodes of this node.
        """
        if self.parent is None:
            return self.data.getName()
        else:
            return self.parent.ancestorString() + self.data.getName()

    def constituentSpanList(self, startIndex: int, constituentSpanList: list):
        """
        Construct recursively the constituent span list of a subtree rooted at this node.

        PARAMETERS
        ----------
        startIndex : int
            Start index of the leftmost leaf node of this subtree.
        constituentSpanList: list
            Returned span list.
        """
        if len(self.children) > 0:
            constituentSpanList.append(ConstituentSpan(self.data, startIndex, startIndex + self.leafCount()))
        total = 0
        for parseNode in self.children:
            parseNode.constituentSpanList(startIndex + total, constituentSpanList)
            total = total + parseNode.leafCount()
