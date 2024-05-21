from ParseTree.ParseTree import ParseTree
from ParseTree.TreeBank import TreeBank


class ParallelTreeBank:

    from_tree_bank: TreeBank
    to_tree_bank: TreeBank

    def __init__(self,
                 folder1: str,
                 folder2: str,
                 pattern: str = None):
        """
        Another constructor for the ParallelTreeBank class. A ParallelTreeBank consists of two treebanks, where each
        sentence appears in both treebanks with possibly different tree structures. Each treebank is stored in a separate
        folder. Both treebanks are read and distinct sentences are removed from the treebanks. In thid constructor, only
        files matching the pattern are read. Pattern is used for matching the extensions such as .train, .test, .dev.
        :param folder1: Folder containing the files for trees in the first treebank.
        :param folder2: Folder containing the files for trees in the second treebank.
        :param pattern: File pattern used for matching. Patterns are usually used for setting the extensions such as
                        .train, .test, .dev.
        """
        self.from_tree_bank = TreeBank(folder1, pattern)
        self.to_tree_bank = TreeBank(folder2, pattern)
        self.removeDifferentTrees()

    def removeDifferentTrees(self):
        """
        Given two treebanks read, the method removes the trees which do not exist in one of the treebanks. At the end,
        we will only have the tree files that exist in both treebanks.
        """
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
        """
        Returns number of sentences in ParallelTreeBank.
        :return: Number of sentences in ParallelTreeBank.
        """
        return self.from_tree_bank.size()

    def fromTree(self, index: int) -> ParseTree:
        """
        Returns the tree at position index in the first treebank.
        :param index: Position of the tree in the first treebank.
        :return: The tree at position index in the first treebank.
        """
        return self.from_tree_bank.get(index)

    def toTree(self, index: int) -> ParseTree:
        """
        Returns the tree at position index in the second treebank.
        :param index: Position of the tree in the second treebank.
        :return: The tree at position index in the second treebank.
        """
        return self.to_tree_bank.get(index)

    def fromTreeBank(self) -> TreeBank:
        """
        Returns the first treebank.
        :return: First treebank.
        """
        return self.from_tree_bank

    def toTreeBank(self) -> TreeBank:
        """
        Returns the second treebank.
        :return: Second treebank.
        """
        return self.to_tree_bank
