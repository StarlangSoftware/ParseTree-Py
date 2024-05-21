from ParseTree.Symbol import Symbol


class ConstituentSpan:

    __constituent: Symbol
    __start: int
    __end: int

    def __init__(self,
                 constituent: Symbol,
                 start: int,
                 end: int):
        """
        Constructor for the ConstituentSpan class. ConstituentSpan is a structure for storing constituents or phrases in
        a sentence with a specific label. Sets the attributes.
        :param constituent: Label of the span.
        :param start: Start index of the span.
        :param end: End index of the span.
        """
        self.__constituent = constituent
        self.__start = start
        self.__end = end

    def getStart(self) -> int:
        """
        Accessor for the start attribute
        :return: Current start
        """
        return self.__start

    def getEnd(self) -> int:
        """
        Accessor for the end attribute
        :return: Current end
        """
        return self.__end

    def getConstituent(self) -> Symbol:
        """
        Accessor for the constituent attribute
        :return: Current constituent
        """
        return self.__constituent