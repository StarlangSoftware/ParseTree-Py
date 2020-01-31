from __future__ import annotations

from ParseTree.SearchDirectionType import SearchDirectionType
from ParseTree.Symbol import Symbol


class ParseNode:

    children: list
    parent: ParseNode
    data: Symbol

    ADJP = ["NNS", "QP", "NN", "$", "ADVP", "JJ", "VBN", "VBG", "ADJP", "JJR", "NP", "JJS", "DT", "FW", "RBR", "RBS", "SBAR", "RB"]
    ADVP = ["RB", "RBR", "RBS", "FW", "ADVP", "TO", "CD", "JJR", "JJ", "IN", "NP", "JJS", "NN"]
    CONJP = ["CC", "RB", "IN"]
    FRAG = []
    INTJ = []
    LST = ["LS", ":"]
    NAC = ["NN", "NNS", "NNP", "NNPS", "NP", "NAC", "EX", "$", "CD", "QP", "PRP", "VBG", "JJ", "JJS", "JJR", "ADJP", "FW"]
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

    """
    Another simple constructor for ParseNode. It takes inputs left and right children of this node, and the data.
    Sets the corresponding attributes with these inputs.

    PARAMETERS
    ----------
    data : Symbol
        Data for this node.
    left : ParseNode
        Left child of this node.
    right : ParseNode
        Right child of this node.
    """
    def __init__(self, dataOrParent, leftOrLine = None, rightOrIsLeaf = None):
        self.children = []
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
        elif isinstance(dataOrParent, ParseNode) and isinstance(leftOrLine, str) and isinstance(rightOrIsLeaf, bool):
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

    """
    Extracts the head of the children of this current node.

    PARAMETERS
    ----------
    priorityList : list
        Depending on the pos of current node, the priorities among the children are given with this parameter
    direction : SearchDirectionType
        Depending on the pos of the current node, search direction is either from left to right, or from right to left.
    defaultCase : bool
        If true, and no child appears in the priority list, returns first child on the left, or first child on the right 
        depending on the search direction.
        
    RETURNS
    -------
    ParseNode
        Head node of the children of the current node
    """
    def searchHeadChild(self, priorityList: list, direction: SearchDirectionType, defaultCase: bool) -> ParseNode:
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

    """
    If current node is not a leaf, it has one or more children, this method determines recursively the head of
    that (those) child(ren). Otherwise, it returns itself. In this way, this method returns the head of all leaf
    successors.

    RETURNS
    -------
    ParseNode
        Head node of the descendant leaves of this current node.
    """
    def headLeaf(self) -> ParseNode:
        if len(self.children) > 0:
            head = self.headChild()
            if head is not None:
                return head.headLeaf()
            else:
                return None
        else:
            return self

    """
    Calls searchHeadChild to determine the head node of all children of this current node. The search direction and
    the search priority list is determined according to the symbol in this current parent node.

    RETURNS
    -------
    ParseNode
        Head node among its children of this current node.
    """
    def headChild(self) -> ParseNode:
        if self.data.trimSymbol().__str__() == "ADJP":
            return self.searchHeadChild(self.ADJP, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "ADVP":
            return self.searchHeadChild(self.ADVP, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "CONJP":
            return self.searchHeadChild(self.CONJP, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "FRAG":
            return self.searchHeadChild(self.FRAG, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "INTJ":
            return self.searchHeadChild(self.INTJ, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "LST":
            return self.searchHeadChild(self.LST, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "NAC":
            return self.searchHeadChild(self.NAC, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "PP":
            return self.searchHeadChild(self.PP, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "PRN":
            return self.searchHeadChild(self.PRN, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "PRT":
            return self.searchHeadChild(self.PRT, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "QP":
            return self.searchHeadChild(self.QP, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "RRC":
            return self.searchHeadChild(self.RRC, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "S":
            return self.searchHeadChild(self.S, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "SBAR":
            return self.searchHeadChild(self.SBAR, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "SBARQ":
            return self.searchHeadChild(self.SBARQ, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "SINV":
            return self.searchHeadChild(self.SINV, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "SQ":
            return self.searchHeadChild(self.SQ, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "UCP":
            return self.searchHeadChild(self.UCP, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "VP":
            return self.searchHeadChild(self.VP, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "WHADJP":
            return self.searchHeadChild(self.WHADJP, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "WHADVP":
            return self.searchHeadChild(self.WHADVP, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "WHNP":
            return self.searchHeadChild(self.WHNP, SearchDirectionType.LEFT, True)
        elif self.data.trimSymbol().__str__() == "WHPP":
            return self.searchHeadChild(self.WHPP, SearchDirectionType.RIGHT, True)
        elif self.data.trimSymbol().__str__() == "NP":
            if self.lastChild().getData().getName() == "POS":
                return self.lastChild()
            else:
                result = self.searchHeadChild(self.NP1, SearchDirectionType.RIGHT, False)
                if result is not None:
                    return result
                else:
                    result = self.searchHeadChild(self.NP2, SearchDirectionType.LEFT, False)
                    if result is not None:
                        return result
                    else:
                        result = self.searchHeadChild(self.NP3, SearchDirectionType.RIGHT, False)
                        if result is not None:
                            return result
                        else:
                            result = self.searchHeadChild(self.NP4, SearchDirectionType.RIGHT, False)
                            if result is not None:
                                return result
                            else:
                                result = self.searchHeadChild(self.NP5, SearchDirectionType.RIGHT, False)
                                if result is not None:
                                    return result
                                else:
                                    return self.lastChild()
        return None

    """
    Adds a child node at the end of the children node list.

    PARAMETERS
    ----------
    child : ParseNode
        Child node to be added.
    """
    def addChild(self, child: ParseNode, index=None):
        if index is None:
            self.children.append(child)
        else:
            self.children.insert(index, child)
        child.parent = self

    """
    Recursive method to restore the parents of all nodes below this node in the hierarchy.
    """
    def correctParents(self):
        for child in self.children:
            child.parent = self
            child.correctParents()

    """
    Recursive method to remove all nodes starting with the symbol X. If the node is removed, its children are
    connected to the next sibling of the deleted node.
    """
    def removeXNodes(self):
        i = 0
        while i < len(self.children):
            if self.children[i].getData().getName().startswith("X"):
                self.children.insert(i + 1, self.children[i].children)
                self.children.pop(i)
            else:
                i = i + 1
        for child in self.children:
            child.removeXNodes()

    """
    Replaces a child node at the given specific with a new child node.

    PARAMETERS
    ----------
    index : int
        Index where the new child node replaces the old one.
    child : ParseNode
        Child node to be replaced.
    """
    def setChild(self, index: int, child: ParseNode):
        self.children[index] = child

    """
    Removes a given child from children node list.

    PARAMETERS
    ----------
    child : ParseNode
        Child node to be deleted.
    """
    def removeChild(self, child: ParseNode):
        self.children.remove(child)

    """
    Recursive method to calculate the number of all leaf nodes in the subtree rooted with this current node.

    RETURNS
    -------
    int
        Number of all leaf nodes in the current subtree.
    """
    def leafCount(self) -> int:
        if len(self.children) == 0:
            return 1
        else:
            total = 0
            for child in self.children:
                total += child.leafCount()
            return total

    """
    Recursive method to calculate the number of all nodes in the subtree rooted with this current node.

    RETURNS
    -------
    int
        Number of all nodes in the current subtree.
    """
    def nodeCount(self) -> int:
        if len(self.children) > 0:
            total = 1
            for child in self.children:
                total += child.nodeCount()
            return total
        else:
            return 1

    """
    Recursive method to calculate the number of all nodes, which have more than one children, in the subtree rooted
    with this current node.

    RETURNS
    -------
    int
        Number of all nodes, which have more than one children, in the current subtree.
    """
    def nodeCountWithMultipleChildren(self) -> int:
        if len(self.children) > 1:
            total = 1
            for child in self.children:
                total += child.nodeCountWithMultipleChildren()
            return total
        else:
            return 0

    """
    Returns number of children of this node.

    RETURNS
    -------
    int
        Number of children of this node.
    """
    def numberOfChildren(self) -> int:
        return len(self.children)

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
    def getChild(self, i: int) -> ParseNode:
        return self.children[i]

    """
    Returns the first child of this node.

    RETURNS
    -------
    ParseNode
        First child of this node.
    """
    def firstChild(self) -> ParseNode:
        return self.children[0]

    """
    Returns the last child of this node.

    RETURNS
    -------
    ParseNode
        Last child of this node.
    """
    def lastChild(self) -> ParseNode:
        return self.children[len(self.children) - 1]