from ParseTree.ParseTree import ParseTree
from ParseTree.TreeBank import TreeBank


class ParallelTreeBank:

    __fromTreeBank: TreeBank
    __toTreeBank: TreeBank

    def __init__(self, folder1: str, folder2: str, pattern: str = None):
        self.__fromTreeBank = TreeBank(folder1, pattern)
        self.__toTreeBank = TreeBank(folder2, pattern)
        self.removeDifferentTrees()

    def removeDifferentTrees(self):
        i = 0
        j = 0
        while i < self.__fromTreeBank.size() and j < self.__toTreeBank.size():
            if self.__fromTreeBank.get(i).getName() < self.__toTreeBank.get(j).getName():
                self.__fromTreeBank.removeTree(i)
            elif self.__fromTreeBank.get(i).getName() > self.__toTreeBank.get(j).getName():
                self.__toTreeBank.removeTree(j)
            else:
                i = i + 1
                j = j + 1
        while i < self.__fromTreeBank.size():
            self.__fromTreeBank.removeTree(i)
        while j < self.__toTreeBank.size():
            self.__toTreeBank.removeTree(j)

    def size(self) -> int:
        return self.__fromTreeBank.size()

    def fromTree(self, index: int) -> ParseTree:
        return self.__fromTreeBank.get(index)

    def toTree(self, index: int) -> ParseTree:
        return self.__toTreeBank.get(index)

    def fromTreeBank(self) -> TreeBank:
        return self.__fromTreeBank

    def toTreeBank(self) -> TreeBank:
        return self.__toTreeBank
