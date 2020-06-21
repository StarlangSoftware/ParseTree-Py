import unittest

from ParseTree.TreeBank import TreeBank


class TreeBankTest(unittest.TestCase):

    def test_TreeBank(self):
        treeBank1 = TreeBank("../trees")
        self.assertEqual(5, treeBank1.size())
        self.assertEqual(30, treeBank1.wordCount(True))
        treeBank2 = TreeBank("../trees", ".dev")
        self.assertEqual(5, treeBank2.size())
        self.assertEqual(30, treeBank2.wordCount(True))


if __name__ == '__main__':
    unittest.main()
