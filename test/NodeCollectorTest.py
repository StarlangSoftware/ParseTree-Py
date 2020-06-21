import unittest

from ParseTree.NodeCollector import NodeCollector
from ParseTree.NodeCondition.IsEnglishLeaf import IsEnglishLeaf
from ParseTree.NodeCondition.IsLeaf import IsLeaf
from ParseTree.ParseTree import ParseTree


class NodeCollectorTest(unittest.TestCase):

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

    def test_CollectLeaf(self):
        nodeCollector1 = NodeCollector(self.parseTree1.getRoot(), IsLeaf())
        self.assertEqual(13, len(nodeCollector1.collect()))
        nodeCollector1 = NodeCollector(self.parseTree2.getRoot(), IsLeaf())
        self.assertEqual(15, len(nodeCollector1.collect()))
        nodeCollector1 = NodeCollector(self.parseTree3.getRoot(), IsLeaf())
        self.assertEqual(10, len(nodeCollector1.collect()))
        nodeCollector1 = NodeCollector(self.parseTree4.getRoot(), IsLeaf())
        self.assertEqual(10, len(nodeCollector1.collect()))
        nodeCollector1 = NodeCollector(self.parseTree5.getRoot(), IsLeaf())
        self.assertEqual(4, len(nodeCollector1.collect()))

    def test_CollectEnglish(self):
        nodeCollector1 = NodeCollector(self.parseTree1.getRoot(), IsEnglishLeaf())
        self.assertEqual(13, len(nodeCollector1.collect()))
        nodeCollector1 = NodeCollector(self.parseTree2.getRoot(), IsEnglishLeaf())
        self.assertEqual(15, len(nodeCollector1.collect()))
        nodeCollector1 = NodeCollector(self.parseTree3.getRoot(), IsEnglishLeaf())
        self.assertEqual(9, len(nodeCollector1.collect()))
        nodeCollector1 = NodeCollector(self.parseTree4.getRoot(), IsEnglishLeaf())
        self.assertEqual(10, len(nodeCollector1.collect()))
        nodeCollector1 = NodeCollector(self.parseTree5.getRoot(), IsEnglishLeaf())
        self.assertEqual(4, len(nodeCollector1.collect()))


if __name__ == '__main__':
    unittest.main()
