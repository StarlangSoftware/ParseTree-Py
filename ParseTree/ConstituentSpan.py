from ParseTree.Symbol import Symbol


class ConstituentSpan:

    __constituent: Symbol
    __start: int
    __end: int

    def __init__(self,
                 constituent: Symbol,
                 start: int,
                 end: int):
        self.__constituent = constituent
        self.__start = start
        self.__end = end

    def getStart(self) -> int:
        return self.__start

    def getEnd(self) -> int:
        return self.__end

    def getConstituent(self) -> Symbol:
        return self.__constituent