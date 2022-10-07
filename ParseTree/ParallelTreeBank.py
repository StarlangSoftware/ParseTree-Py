from ParseTree.ParseTree import ParseTree
from ParseTree.TreeBank import TreeBank


class ParallelTreeBank:

    from_tree_bank: TreeBank
    to_tree_bank: TreeBank

    def __init__(self,
                 folder1: str,
                 folder2: str,
                 pattern: str = None):
        self.from_tree_bank = TreeBank(folder1, pattern)
        self.to_tree_bank = TreeBank(folder2, pattern)
        self.removeDifferentTrees()

    def removeDifferentTrees(self):
        i = 0
        j = 0
        while i < self.from_tree_bank.size() and j < self.to_tree_bank.size():
            if self.from_tree_bank.get(i).getName() < self.to_tree_bank.get(j).getName():
                self.from_tree_bank.removeTree(i)
            elif self.from_tree_bank.get(i).getName() > self.to_tree_bank.get(j).getName():
                self.to_tree_bank.removeTree(j)
            else:
                i = i + 1
                j = j + 1
        while i < self.from_tree_bank.size():
            self.from_tree_bank.removeTree(i)
        while j < self.to_tree_bank.size():
            self.to_tree_bank.removeTree(j)

    def size(self) -> int:
        return self.from_tree_bank.size()

    def fromTree(self, index: int) -> ParseTree:
        return self.from_tree_bank.get(index)

    def toTree(self, index: int) -> ParseTree:
        return self.to_tree_bank.get(index)

    def fromTreeBank(self) -> TreeBank:
        return self.from_tree_bank

    def toTreeBank(self) -> TreeBank:
        return self.to_tree_bank
