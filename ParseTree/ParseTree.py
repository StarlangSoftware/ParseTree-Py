import os

from ParseTree.NodeCollector import NodeCollector
from ParseTree.NodeCondition.IsEnglishLeaf import IsEnglishLeaf
from ParseTree.ParseNode import ParseNode


class ParseTree:

    sentence_labels = ["SINV", "SBARQ", "SBAR", "SQ", "S"]
    root: ParseNode
    name: str

    def constructor1(self, root: ParseNode):
        """
        Basic constructor for a ParseTree. Initializes the root node with the input.
        :param root: Root node of the tree
        """
        self.root = root

    def constructor2(self, fileName: str):
        """
        Another constructor of the ParseTree. The method takes the file containing a single line as input and constructs
        the whole tree by calling the ParseNode constructor recursively.
        :param fileName: File containing a single line for a ParseTree
        """
        self.name = os.path.split(fileName)[1]
        input_file = open(fileName, "r", encoding="utf8")
        line = input_file.readline()
        if "(" in line and ")" in line:
            line = line[line.index("(") + 1:line.rindex(")")].strip()
            self.root = ParseNode(None, line, False)
        else:
            self.root = None
        input_file.close()

    def __init__(self, rootOrFileName=None):
        """
        Basic constructor for a ParseTree. Initializes the root node with the input.

        PARAMETERS
        ----------
        rootOrFileName : ParseNode
            Root node of the tree
        """
        if isinstance(rootOrFileName, ParseNode):
            self.constructor1(rootOrFileName)
        elif isinstance(rootOrFileName, str):
            self.constructor2(rootOrFileName)

    def nextLeafNode(self, parseNode: ParseNode) -> ParseNode:
        """
        Gets the next leaf node after the given leaf node in the ParseTree.

        PARAMETERS
        ----------
        parseNode : ParseNode
            ParseNode for which next node is calculated.

        RETURNS
        -------
        ParseNode
            Next leaf node after the given leaf node.
        """
        node_collector = NodeCollector(self.root, IsEnglishLeaf())
        leaf_list = node_collector.collect()
        for i in range(len(leaf_list) - 1):
            if leaf_list[i] == parseNode:
                return leaf_list[i + 1]
        return None

    def previousLeafNode(self, parseNode: ParseNode) -> ParseNode:
        """
        Gets the previous leaf node before the given leaf node in the ParseTree.

        PARAMETERS
        ----------
        parseNode : ParseNode
            ParseNode for which previous node is calculated.

        RETURNS
        -------
        ParseNode
            Previous leaf node before the given leaf node.
        """
        node_collector = NodeCollector(self.root, IsEnglishLeaf())
        leaf_list = node_collector.collect()
        for i in range(1, len(leaf_list)):
            if leaf_list[i] == parseNode:
                return leaf_list[i - 1]
        return None

    def nodeCountWithMultipleChildren(self) -> int:
        """
        Calls recursive method to calculate the number of all nodes, which have more than one children.

        RETURNS
        -------
        int
            Number of all nodes, which have more than one children.
        """
        return self.root.nodeCountWithMultipleChildren()

    def setName(self, name: str):
        """
        Mutator for the name attribute.
        :param name: Name of the parse tree.
        """
        self.name = name

    def getName(self) -> str:
        """
        Accessor for the name attribute.
        :return: Name of the parse tree.
        """
        return self.name

    def nodeCount(self) -> int:
        """
        Calls recursive method to calculate the number of all nodes tree.

        RETURNS
        -------
        int
            Number of all nodes in the tree.
        """
        return self.root.nodeCount()

    def leafCount(self) -> int:
        """
        Calls recursive method to calculate the number of all leaf nodes in the tree.

        RETURNS
        -------
        int
            Number of all leaf nodes in the tree.
        """
        return self.root.leafCount()

    def isFullSentence(self) -> bool:
        if self.root is not None and self.root.data.getName() in self.sentence_labels:
            return True
        return False

    def save(self, fileName: str):
        """
        Saves the tree into the file with the given file name. The output file only contains one line representing tree.

        PARAMETERS
        ----------
        fileName : str
            Output file name
        """
        output_file = open(fileName, "w", encoding="utf8")
        output_file.write("( " + self.__str__() + " )\n")
        output_file.close()

    def correctParents(self):
        """
        Calls recursive method to restore the parents of all nodes in the tree.
        """
        self.root.correctParents()

    def removeXNodes(self):
        """
        Calls recursive method to remove all nodes starting with the symbol X. If the node is removed, its children are
        connected to the next sibling of the deleted node.
        """
        self.root.removeXNodes()

    def getRoot(self) -> ParseNode:
        """
        Accessor method for the root node.

        RETURNS
        -------
        ParseNode
            Root node
        """
        return self.root

    def __str__(self) -> str:
        """
        Calls recursive function to convert the tree to a string.

        RETURNS
        -------
        str
            A string which contains all words in the tree.
        """
        return self.root.__str__()

    def wordCount(self, excludeStopWords: bool) -> int:
        """
        Calls recursive function to count the number of words in the tree.

        PARAMETERS
        ----------
        excludeStopWords : bool
            If true, stop words are not counted.

        RETURNS
        -------
        int
            Number of words in the tree.
        """
        return self.root.wordCount(excludeStopWords)

    def constituentSpanList(self) -> list:
        """
        Generates a list of constituents in the parse tree and their spans.

        RETURNS
        -------
        list
            A list of constituents in the parse tree and their spans.
        """
        result = []
        self.root.constituentSpanList(1, result)
        return result
