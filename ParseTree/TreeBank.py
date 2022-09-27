import os
import re

from ParseTree.ParseTree import ParseTree


class TreeBank:

    __parse_trees: list

    def __init__(self,
                 folder: str = None,
                 pattern: str = None):
        """
        A constructor of TreeBank class which reads all ParseTree files with the file name satisfying the
        given pattern inside the given folder. For each file inside that folder, the constructor creates a ParseTree
        and puts in inside the list parseTrees.

        PARAMETERS
        ----------
        folder : str
            Folder where all parseTrees reside.
        pattern : str
            File pattern such as "." ".train" ".test".
        """
        self.__parse_trees = []
        if folder is not None:
            for root, dirs, files in os.walk(folder):
                files.sort()
                for file in files:
                    file_name = os.path.join(root, file)
                    if (pattern is None or pattern in file_name) and re.match("\\d+\\.", file):
                        parseTree = ParseTree(file_name)
                        self.__parse_trees.append(parseTree)

    def size(self) -> int:
        """
        Returns number of trees in the TreeBank.

        RETURNS
        -------
        int
            Number of trees in the TreeBank.
        """
        return len(self.__parse_trees)

    def wordCount(self, excludeStopWords: bool) -> int:
        """
        Returns number of words in the parseTrees in the TreeBank. If excludeStopWords is true, stop words are not
        counted.

        PARAMETERS
        ----------
        excludeStopWords : bool
            If true, stop words are not included in the count process.

        RETURNS
        -------
        int
            Number of all words in all parseTrees in the TreeBank.
        """
        total = 0
        for tree in self.__parse_trees:
            total += tree.wordCount(excludeStopWords)
        return total

    def get(self, index: int) -> ParseTree:
        """
        Accessor for a single ParseTree.

        PARAMETERS
        ----------
        index : int
            Index of the parseTree.

        RETURNS
        -------
        ParseTree
            The ParseTree at the given index.
        """
        return self.__parse_trees[index]

    def removeTree(self, i):
        self.__parse_trees.pop(i)
