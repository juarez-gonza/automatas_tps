import re

from grammar_symbols import *

class Token(Grammar_Symbol):
    token_patterns = [
        #re.compile("[a-zA-Z_]+"),   # ID -> [a-zA-Z_]+
        re.compile("[0-9]+"),       # NUM -> [0-9]+
        re.compile("\+"),           # SUM -> +
        re.compile("\*"),           # MUL -> *
        re.compile("\("),           # O_PAREN -> (
        re.compile("\)"),           # C_PAREN -> )
        re.compile("\$")            # END_SYM -> $
    ]

    def __init__(self, name, value, attr=None):
        self.attr = attr
        super().__init__(name, value)

    @staticmethod
    def gen(c):
        #if Token.token_patterns[0].match(c):
        #    return Token(TERM.ID.name, TERM.ID.value, c)
        if Token.token_patterns[0].match(c):
            return Token(TERM.NUM.name, TERM.NUM.value, float(c))
        elif Token.token_patterns[1].match(c):
            return Token(TERM.SUM.name, TERM.SUM.value)
        elif Token.token_patterns[2].match(c):
            return Token(TERM.MUL.name, TERM.MUL.value)
        elif Token.token_patterns[3].match(c):
            return Token(TERM.O_PAREN.name, TERM.O_PAREN.value)
        elif Token.token_patterns[4].match(c):
            return Token(TERM.C_PAREN.name, TERM.C_PAREN.value)
        elif Token.token_patterns[5].match(c):
            return Token(TERM.END_SYM.name, TERM.END_SYM.value)

class Token_Stream():
    def __init__(self, inp):
        self.token_stream = [Token.gen(c) for c in inp]
        self.token_stream.append(Token.gen("$"))
        self.idx = 0

    def get_next_token(self):
        ret = None
        if self.idx < len(self.token_stream):
            ret = self.token_stream[self.idx]
            self.idx += 1
        return ret
