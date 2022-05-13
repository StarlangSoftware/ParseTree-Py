import unittest

from ParseTree.ParallelTreeBank import ParallelTreeBank


class ParallelTreeBankTest(unittest.TestCase):

    def test_ParallelTreeBank(self):
        parallelTreeBank = ParallelTreeBank("../trees", "../trees2")
        self.assertEqual(3, parallelTreeBank.size())


if __name__ == '__main__':
    unittest.main()
