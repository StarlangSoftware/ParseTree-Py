from abc import abstractmethod

from ParseTree.ParseNode import ParseNode


class NodeCondition:

    @abstractmethod
    def satisfies(self, parseNode: ParseNode) -> bool:
        pass
