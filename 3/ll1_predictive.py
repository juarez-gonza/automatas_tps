#!/usr/bin/env python3
import enum
import re

# Compilers: Principles, Techniques, & Tools - 2nd Edition
#       4.4.4: Nonrecursive Predictive Parsing

# ===================== GRAMMAR-SYMBOL INTERFACE (== Enum interface) =====================
class Grammar_Symbol():
    def __init__(self, name, value):
        self.name = name
        self.value = value

# ===================== LEXER =====================

# TERMINAL (INPUT SYMBOL)
class TERM(enum.Enum):
    NUM = 0
    SUM = 1
    MUL = 2
    O_PAREN = 3
    C_PAREN = 4
    END_SYM = 5
    EMPTY = 6

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
    def gen_token(c):
        #if Token.token_patterns[0].match(c):
        #    return Token(TERM.ID.name, TERM.ID.value, c)
        if Token.token_patterns[0].match(c):
            return Token(TERM.NUM.name, TERM.NUM.value, c)
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
        self.token_stream = [Token.gen_token(c) for c in inp]
        self.token_stream.append(Token.gen_token("$"))
        self.idx = 0

    def get_next_token(self):
        ret = None
        if self.idx < len(self.token_stream):
            ret = self.token_stream[self.idx]
            self.idx += 1
        return ret

# ===================== PARSER =====================

# NON-TERMINAL
class NTERM(enum.Enum):
    E = 0
    E_ = 1
    T = 2
    T_ = 3
    F = 4

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

#       NON-TERMINAL   |  INPUT SYMBOL
#                      |  [0] = num     [1] = +     [2] = *     [3] = (         [4] = )     [5] = $
#       ptable[0] = E  |  ["E->TE'",    "",         "",         "E->TE'",       "",         ""],
#       ptable[1] = E' |  ["",          "E'->+TE'", "",         "",             "E'->e",    "E'->e"],
#       ptable[2] = T  |  ["T->FT'",    "",         "",         "T->FT'",       "",         ""],
#       ptable[3] = T' |  ["",          "T'->e",    "T->*FT'",  "",             "T'->e",    "T'->e"],
#       ptable[4] = F  |  ["F->num",    "",         "",         "F->(E)",       "",         ""],

class Parser():
    def __init__(self, token_stream):
        self.token_stream = token_stream
        self.ptable = [
            [[NTERM.T, NTERM.E_],   [],                             [],                                         [NTERM.T, NTERM.E_],                        [],                 []],
            [[],                    [TERM.SUM, NTERM.T, NTERM.E_],  [],                                         [],                                         [TERM.EMPTY],       [TERM.EMPTY]],
            [[NTERM.F, NTERM.T_],   [],                             [],                                         [NTERM.F, NTERM.T_],                        [],                 []],
            [[],                    [TERM.EMPTY],                   [TERM.MUL, NTERM.F, NTERM.T_],              [],                                         [TERM.EMPTY],       [TERM.EMPTY]],
            [[TERM.NUM],            [],                             [],                                         [TERM.O_PAREN, NTERM.E, TERM.C_PAREN],      [],                 []],
        ]

        self.s_sym = NTERM.E
        self.end_sym = Token.gen_token("$")
        self.stack = Stack()
        self.stack.push(self.end_sym)
        self.stack.push(self.s_sym)

    def predictive(self):
        X = self.stack.top()
        a = self.token_stream.get_next_token()

        while X.name != self.end_sym.name:
            if X.name == a.name:
                print("\t====Match de token X = %s (%d), a = %s (%d)====" % (X.name, X.value, a.name, a.value))
                self.stack.pop()
                a = self.token_stream.get_next_token()
            elif isinstance(X, Token):
                raise ValueError("Un token no debería llegar hasta aquí. X: name=%s value=%d attr=%s" % (X.name, X.value, X.attr))
            elif not self.ptable[X.value][a.value]:
                raise ValueError("No hay entrada para X = %s (%d), a = %s (%d)" % (X.name, X.value, a.name, a.value))
            else:
                print("Match de entrada para X = %s (%d), a = %s (%d)" % (X.name, X.value, a.name, a.value))
                production = self.ptable[X.value][a.value]
                self.stack.pop()
                self.push_production(production)
            X = self.stack.top()
        print("\t====Match de símbolo de finalización X = %s, a = %s====" % (X.name, a.name))

    def push_production(self, production):
        if production[0] == TERM.EMPTY:
            return
        for i in range(len(production) - 1, -1, -1):
            grammar_sym = production[i]
            self.stack.push(grammar_sym)


if __name__ == "__main__":
    #inp = input()
    inp = "7+3*4"
    token_stream = Token_Stream(inp)
    parser = Parser(token_stream)
    parser.predictive()
