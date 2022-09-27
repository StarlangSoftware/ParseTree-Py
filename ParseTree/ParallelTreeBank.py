from ParseTree.ParseTree import ParseTree
from ParseTree.TreeBank import TreeBank


class ParallelTreeBank:

    __from_tree_bank: TreeBank
    __to_tree_bank: TreeBank

    def __init__(self,
                 folder1: str,
                 folder2: str,
                 pattern: str = None):
        self.__from_tree_bank = TreeBank(folder1, pattern)
        self.__to_tree_bank = TreeBank(folder2, pattern)
        self.removeDifferentTrees()

    def removeDifferentTrees(self):
        i = 0
        j = 0
        while i < self.__from_tree_bank.size() and j < self.__to_tree_bank.size():
            if self.__from_tree_bank.get(i).getName() < self.__to_tree_bank.get(j).getName():
                self.__from_tree_bank.removeTree(i)
            elif self.__from_tree_bank.get(i).getName() > self.__to_tree_bank.get(j).getName():
                self.__to_tree_bank.removeTree(j)
            else:
                i = i + 1
                j = j + 1
        while i < self.__from_tree_bank.size():
            self.__from_tree_bank.removeTree(i)
        while j < self.__to_tree_bank.size():
            self.__to_tree_bank.removeTree(j)

    def size(self) -> int:
        return self.__from_tree_bank.size()

    def fromTree(self, index: int) -> ParseTree:
        return self.__from_tree_bank.get(index)

    def toTree(self, index: int) -> ParseTree:
        return self.__to_tree_bank.get(index)

    def fromTreeBank(self) -> TreeBank:
        return self.__from_tree_bank

    def toTreeBank(self) -> TreeBank:
        return self.__to_tree_bank
