from ParseTree.NodeCondition.NodeCondition import NodeCondition
from ParseTree.ParseNode import ParseNode


class NodeCollector:

    condition: NodeCondition
    rootNode: ParseNode

    def __init__(self, rootNode: ParseNode, condition: NodeCondition):
        """
        Constructor for the NodeCollector class. NodeCollector's main aim is to collect a set of ParseNode's from a
        subtree rooted at rootNode, where the ParseNode's satisfy a given NodeCondition, which is implemented by other
        interface class.

        PARAMETERS
        ----------
        rootNode : ParseNode
            Root node of the subtree
        condition : NodeCondition
            The condition interface for which all nodes in the subtree rooted at rootNode will be checked
        """
        self.rootNode = rootNode
        self.condition = condition

    def __collectNodes(self, parseNode: ParseNode, collected: list):
        """
        Private recursive method to check all descendants of the parseNode, if they ever satisfy the given node
        condition

        PARAMETERS
        ----------
        parseNode : ParseNode
            Root node of the subtree
        collected : list
            The list where the collected ParseNode's will be stored.
        """
        if self.condition.satisfies(parseNode):
            collected.append(parseNode)
        else:
            for child in parseNode.children:
                self.__collectNodes(child, collected)

    def collect(self) -> list:
        """
        Collects and returns all ParseNode's satisfying the node condition.

        RETURNS
        -------
        list
            All ParseNode's satisfying the node condition.
        """
        result = []
        self.__collectNodes(self.rootNode, result)
        return result
