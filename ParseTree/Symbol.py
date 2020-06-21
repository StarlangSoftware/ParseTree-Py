from __future__ import annotations
from Dictionary.Word import Word


class Symbol(Word):
    nonTerminalList = ["ADJP", "ADVP", "CC", "CD", "CONJP", "DT", "EX", "FRAG", "FW", "IN", "INTJ", "JJ", "JJR", "JJS",
                       "LS", "LST", "MD", "NAC", "NN", "NNP", "NNPS", "NNS", "NP", "NX", "PDT", "POS", "PP", "PRN",
                       "PRP", "PRP$", "PRT", "PRT|ADVP", "QP", "RB", "RBR", "RP", "RRC", "S", "SBAR", "SBARQ", "SINV",
                       "SQ", "SYM", "TO", "UCP", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "VP", "WDT", "WHADJP",
                       "WHADVP", "WHNP", "WP", "WP$", "WRB", "X", "-NONE-"]

    phraseLabels = ["NP", "PP", "ADVP", "ADJP", "CC", "VG"]

    sentenceLabels = ["SINV", "SBARQ", "SBAR", "SQ", "S"]

    verbLabels = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "VERB"]

    VPLabel = "VP"

    def __eq__(self, other):
        return self.name == other.name

    def __init__(self, name: str):
        """
        Constructor for Symbol class. Sets the name attribute.

        PARAMETERS
        ----------
        name : str
            Name attribute
        """
        super().__init__(name)

    def isVP(self) -> bool:
        """
        Checks if the symbol is VP or not.

        RETURNS
        -------
        bool
            True if the symbol is VB, false otherwise.
        """
        return self.name == self.VPLabel

    def isTerminal(self) -> bool:
        """
        Checks if this symbol is a terminal symbol or not. A symbol is terminal if it is a punctuation symbol, or
        if it starts with a lowercase symbol.

        RETURNS
        -------
        bool
            True if this symbol is a terminal symbol, false otherwise.
        """
        if self.name == "," or self.name == "." or self.name == "!" or self.name == "?" or self.name == ":" \
                or self.name == ";" or self.name == "\"" or self.name == "''" or self.name == "'" or self.name == "`" \
                or self.name == "``" or self.name == "..." or self.name == "-" or self.name == "--":
            return True
        if self.name in self.nonTerminalList:
            return False
        if self.name == "I" or self.name == "A":
            return True
        for ch in self.name:
            if 'a' <= ch <= 'z':
                return True
        return False

    def isChunkLabel(self) -> bool:
        """
        Checks if this symbol can be a chunk label or not.

        RETURNS
        -------
        bool
            True if this symbol can be a chunk label, false otherwise.
        """
        if Word.isPunctuationSymbol(self.name) or self.name.replace("-.*", "") in self.sentenceLabels or \
                self.name.replace("-.*", "") in self.phraseLabels:
            return True
        return False

    def trimSymbol(self) -> Symbol:
        """
        If the symbol's data contains '-' or '=', this method trims all characters after those characters and returns
        the resulting string.

        RETURNS
        -------
        Symbol
            Trimmed symbol.
        """
        if self.name.startswith("-") or ("-" not in self.name and "=" not in self.name):
            return self
        if "-" in self.name:
            minusIndex = self.name.index("-")
        else:
            minusIndex = -1
        if "=" in self.name:
            equalIndex = self.name.index("=")
        else:
            equalIndex = -1
        if minusIndex != -1 or equalIndex != -1:
            if minusIndex != -1 and equalIndex != -1:
                if minusIndex < equalIndex:
                    return Symbol(self.name[:minusIndex])
                else:
                    return Symbol(self.name[:equalIndex])
            else:
                if minusIndex != -1:
                    return Symbol(self.name[:minusIndex])
                else:
                    return Symbol(self.name[:equalIndex])
        else:
            return self
