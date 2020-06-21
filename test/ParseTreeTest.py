import unittest

from ParseTree.ParseTree import ParseTree


class ParseTreeTest(unittest.TestCase):

    parseTree1 : ParseTree
    parseTree2 : ParseTree
    parseTree3 : ParseTree
    parseTree4 : ParseTree
    parseTree5 : ParseTree

    def setUp(self) -> None:
        self.parseTree1 = ParseTree("../trees/0000.dev")
        self.parseTree2 = ParseTree("../trees/0001.dev")
        self.parseTree3 = ParseTree("../trees/0002.dev")
        self.parseTree4 = ParseTree("../trees/0003.dev")
        self.parseTree5 = ParseTree("../trees/0014.dev")

    def test_NodeCount(self):
        self.assertEqual(34, self.parseTree1.nodeCount())
        self.assertEqual(39, self.parseTree2.nodeCount())
        self.assertEqual(32, self.parseTree3.nodeCount())
        self.assertEqual(28, self.parseTree4.nodeCount())
        self.assertEqual(9, self.parseTree5.nodeCount())

    def test_IsFullSentence(self):
        self.assertTrue(self.parseTree1.isFullSentence())
        self.assertTrue(self.parseTree2.isFullSentence())
        self.assertTrue(self.parseTree3.isFullSentence())
        self.assertTrue(self.parseTree4.isFullSentence())
        self.assertFalse(self.parseTree5.isFullSentence())

    def test_LeafCount(self):
        self.assertEqual(13, self.parseTree1.leafCount())
        self.assertEqual(15, self.parseTree2.leafCount())
        self.assertEqual(10, self.parseTree3.leafCount())
        self.assertEqual(10, self.parseTree4.leafCount())
        self.assertEqual(4, self.parseTree5.leafCount())

    def test_NodeCountWithMultipleChildren(self):
        self.assertEqual(8, self.parseTree1.nodeCountWithMultipleChildren())
        self.assertEqual(9, self.parseTree2.nodeCountWithMultipleChildren())
        self.assertEqual(8, self.parseTree3.nodeCountWithMultipleChildren())
        self.assertEqual(6, self.parseTree4.nodeCountWithMultipleChildren())
        self.assertEqual(1, self.parseTree5.nodeCountWithMultipleChildren())

    def test_WordCount(self):
        self.assertEqual(7, self.parseTree1.wordCount(True))
        self.assertEqual(8, self.parseTree2.wordCount(True))
        self.assertEqual(6, self.parseTree3.wordCount(True))
        self.assertEqual(7, self.parseTree4.wordCount(True))
        self.assertEqual(2, self.parseTree5.wordCount(True))


if __name__ == '__main__':
    unittest.main()
