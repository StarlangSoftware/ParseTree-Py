from __future__ import annotations
from Dictionary.Word import Word


class Symbol(Word):
    non_terminal_list = ["ADJP", "ADVP", "CC", "CD", "CONJP", "DT", "EX", "FRAG", "FW", "IN", "INTJ", "JJ", "JJR", "JJS",
                       "LS", "LST", "MD", "NAC", "NN", "NNP", "NNPS", "NNS", "NP", "NX", "PDT", "POS", "PP", "PRN",
                       "PRP", "PRP$", "PRT", "PRT|ADVP", "QP", "RB", "RBR", "RP", "RRC", "S", "SBAR", "SBARQ", "SINV",
                       "SQ", "SYM", "TO", "UCP", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "VP", "WDT", "WHADJP",
                       "WHADVP", "WHNP", "WP", "WP$", "WRB", "X", "-NONE-"]

    phrase_labels = ["NP", "PP", "ADVP", "ADJP", "CC", "VG"]

    sentence_labels = ["SINV", "SBARQ", "SBAR", "SQ", "S"]

    verb_labels = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "VERB"]

    vp_label = "VP"

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
        return self.name == self.vp_label

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
        if self.name in self.non_terminal_list:
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
        if Word.isPunctuationSymbol(self.name) or self.name.replace("-.*", "") in self.sentence_labels or \
                self.name.replace("-.*", "") in self.phrase_labels:
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
            minus_index = self.name.index("-")
        else:
            minus_index = -1
        if "=" in self.name:
            equal_index = self.name.index("=")
        else:
            equal_index = -1
        if minus_index != -1 or equal_index != -1:
            if minus_index != -1 and equal_index != -1:
                if minus_index < equal_index:
                    return Symbol(self.name[:minus_index])
                else:
                    return Symbol(self.name[:equal_index])
            else:
                if minus_index != -1:
                    return Symbol(self.name[:minus_index])
                else:
                    return Symbol(self.name[:equal_index])
        else:
            return self
