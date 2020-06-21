from ParseTree.NodeCondition.IsLeaf import IsLeaf
from ParseTree.ParseNode import ParseNode


class IsEnglishLeaf(IsLeaf):

    def satisfies(self, parseNode: ParseNode) -> bool:
        """
        Implemented node condition for English leaf node.

        PARAMETERS
        ----------
        parseNode : ParseNode
            Checked node.

        RETURNS
        -------
        bool
            If the node is a leaf node and is not a dummy node, returns true; false otherwise.
        """
        if super().satisfies(parseNode):
            data = parseNode.getData().getName()
            parentData = parseNode.getParent().getData().getName()
            if "*" in data or (data == "0" and parentData == "-NONE-"):
                return False
            return True
        return False
