from ParseTree.Symbol import Symbol


class ConstituentSpan:

    constituent: Symbol
    start: int
    end: int

    def __init__(self, constituent: Symbol, start: int, end: int):
        self.constituent = constituent
        self.start = start
        self.end = end

    def getStart(self) -> int:
        return self.start

    def getEnd(self) -> int:
        return self.end

    def getConstituent(self) -> Symbol:
        return self.constituent