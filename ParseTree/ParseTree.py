from ParseTree.NodeCollector import NodeCollector
from ParseTree.NodeCondition.IsEnglishLeaf import IsEnglishLeaf
from ParseTree.ParseNode import ParseNode


class ParseTree:

    sentenceLabels = ["SINV", "SBARQ", "SBAR", "SQ", "S"]
    root: ParseNode

    """
    Basic constructor for a ParseTree. Initializes the root node with the input.

    PARAMETERS
    ----------
    root : ParseNode
        Root node of the tree
    """
    def __init__(self, rootOrFileName=None):
        if isinstance(rootOrFileName, ParseNode):
            self.root = rootOrFileName
        elif isinstance(rootOrFileName, str):
            inputFile = open(rootOrFileName, "r", encoding="utf8")
            line = inputFile.readline()
            if "(" in line and ")" in line:
                line = line[line.index("(") + 1:line.rindex(")")].strip()
                self.root = ParseNode(None, line, False)
            else:
                self.root = None
            inputFile.close()

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
    def nextLeafNode(self, parseNode: ParseNode) -> ParseNode:
        nodeCollector = NodeCollector(self.root, IsEnglishLeaf())
        leafList = nodeCollector.collect()
        for i in range(len(leafList) - 1):
            if leafList[i] == parseNode:
                return leafList[i + 1]
        return None

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
    def previousLeafNode(self, parseNode: ParseNode) -> ParseNode:
        nodeCollector = NodeCollector(self.root, IsEnglishLeaf())
        leafList = nodeCollector.collect()
        for i in range(1, len(leafList)):
            if leafList[i] == parseNode:
                return leafList[i - 1]
        return None

    def constructUniversalDependencies(self) -> map:
        universalDependencies = {}
        self.root.constructUniversalDependencies(universalDependencies)
        return universalDependencies

    """
    Calls recursive method to calculate the number of all nodes, which have more than one children.

    RETURNS
    -------
    int
        Number of all nodes, which have more than one children.
    """
    def nodeCountWithMultipleChildren(self) -> int:
        return self.root.nodeCountWithMultipleChildren()

    """
    Calls recursive method to calculate the number of all nodes tree.

    RETURNS
    -------
    int
        Number of all nodes in the tree.
    """
    def nodeCount(self) -> int:
        return self.root.nodeCount()

    """
    Calls recursive method to calculate the number of all leaf nodes in the tree.
    
    RETURNS
    -------
    int
        Number of all leaf nodes in the tree.
    """
    def leafCount(self) -> int:
        return self.root.leafCount()

    def isFullSentence(self) -> bool:
        if self.root is not None and self.root.data.getName() in self.sentenceLabels:
            return True
        return False

    """
    Saves the tree into the file with the given file name. The output file only contains one line representing tree.

    PARAMETERS
    ----------
    fileName : str
        Output file name
    """
    def save(self, fileName: str):
        outputFile = open(fileName, "w", encoding="utf8")
        outputFile.write("( " + self.__str__() + " )\n")
        outputFile.close()

    """
    Calls recursive method to restore the parents of all nodes in the tree.
    """
    def correctParents(self):
        self.root.correctParents()

    """
    Calls recursive method to remove all nodes starting with the symbol X. If the node is removed, its children are
    connected to the next sibling of the deleted node.
    """
    def removeXNodes(self):
        self.root.removeXNodes()

    """
    Accessor method for the root node.

    RETURNS
    -------
    ParseNode
        Root node
    """
    def getRoot(self) -> ParseNode:
        return self.root

    """
    Calls recursive function to convert the tree to a string.

    RETURNS
    -------
    str
        A string which contains all words in the tree.
    """
    def __str__(self) -> str:
        return self.root.__str__()

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
    def wordCount(self, excludeStopWords: bool) -> int:
        return self.root.wordCount(excludeStopWords)
