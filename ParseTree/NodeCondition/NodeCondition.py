from abc import abstractmethod


class NodeCondition:


    @abstractmethod
    def satisfies(self, parseNode: ParseNode) -> bool:
        pass
