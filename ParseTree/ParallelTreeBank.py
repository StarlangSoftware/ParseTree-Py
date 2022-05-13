from ParseTree.ParseTree import ParseTree
from ParseTree.TreeBank import TreeBank


class ParallelTreeBank:

    fromTreeBank: TreeBank
    toTreeBank: TreeBank

    def __init__(self, folder1: str, folder2: str, pattern: str = None):
        self.fromTreeBank = TreeBank(folder1, pattern)
        self.toTreeBank = TreeBank(folder2, pattern)
        self.removeDifferentTrees()

    def removeDifferentTrees(self):
        i = 0
        j = 0
        while i < self.fromTreeBank.size() and j < self.toTreeBank.size():
            if self.fromTreeBank.get(i).getName() < self.toTreeBank.get(j).getName():
                self.fromTreeBank.removeTree(i)
            elif self.fromTreeBank.get(i).getName() > self.toTreeBank.get(j).getName():
                self.toTreeBank.removeTree(j)
            else:
                i = i + 1
                j = j + 1
        while i < self.fromTreeBank.size():
            self.fromTreeBank.removeTree(i)
        while j < self.toTreeBank.size():
            self.toTreeBank.removeTree(j)

    def size(self) -> int:
        return self.fromTreeBank.size()

    def fromTree(self, index: int) -> ParseTree:
        return self.fromTreeBank.get(index)

    def toTree(self, index: int) -> ParseTree:
        return self.toTreeBank.get(index)

    def fromTreeBank(self) -> TreeBank:
        return self.fromTreeBank

    def toTreeBank(self) -> TreeBank:
        return self.toTreeBank
