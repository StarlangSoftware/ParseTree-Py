from ParseTree.NodeCondition.NodeCondition import NodeCondition
from ParseTree.ParseNode import ParseNode


class IsLeaf(NodeCondition):

    """
    Implemented node condition for the leaf node. If a node has no children it is a leaf node.

    PARAMETERS
    ----------
    parseNode : ParseNode
        Checked node.

    RETURNS
    -------
    bool
        True if the input node is a leaf node, false otherwise.
    """
    def satisfies(self, parseNode: ParseNode) -> bool:
        return parseNode.numberOfChildren() == 0
