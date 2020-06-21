import unittest

from ParseTree.Symbol import Symbol


class SymbolTest(unittest.TestCase):

    def test_trimSymbol(self):
        self.assertEqual("NP", Symbol("NP-SBJ").trimSymbol().getName())
        self.assertEqual("VP", Symbol("VP-SBJ-2").trimSymbol().getName())
        self.assertEqual("NNP", Symbol("NNP-SBJ-OBJ-TN").trimSymbol().getName())
        self.assertEqual("S", Symbol("S-SBJ=OBJ").trimSymbol().getName())


if __name__ == '__main__':
    unittest.main()
