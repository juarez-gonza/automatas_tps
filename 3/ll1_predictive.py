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

# ===================== PARSER =====================

# NON-TERMINAL
class NTERM(enum.Enum):
    E = 0
    E_ = 1
    T = 2
    T_ = 3
    F = 4

class Non_Term(Grammar_Symbol):
    def __init__(self, name, value):
        self.leaves = []
        self.interiors = []
        super().__init__(name, value)

    def append_interior(self, childnode):
        self.interiors.append(childnode)

    def append_leaf(self, childnode):
        self.leaves.append(childnode)

    def walk_arithmetic(self, inh=None):
        pass

    @staticmethod
    def gen(nterm):
        if nterm.name == NTERM.E.name:
            return E(nterm.name, nterm.value)
        elif nterm.name == NTERM.E_.name:
            return E_(nterm.name, nterm.value)
        elif nterm.name == NTERM.T.name:
            return T(nterm.name, nterm.value)
        elif nterm.name == NTERM.T_.name:
            return T_(nterm.name, nterm.value)
        elif nterm.name == NTERM.F.name:
            return F(nterm.name, nterm.value)
        else:
            raise ValueError("Cannot generate non terminal @ Non_Term.gen(), no match for nterm")

# E  -> TE'
class E(Non_Term):
    def __init__(self, name, value):
        super().__init__(name, value)

    def walk_arithmetic(self, inh=None):
        val_T = self.interiors[0].walk_arithmetic()
        val_E_ = self.interiors[1].walk_arithmetic(val_T)
        return val_E_

# E' -> +TE | e
class E_(Non_Term):
    def __init__(self, name, value):
        super().__init__(name, value)

    def walk_arithmetic(self, inh=None):
        if not self.interiors:
            return inh
        val_T = self.interiors[0].walk_arithmetic()
        val_E_ = self.interiors[1].walk_arithmetic(inh + val_T)
        return val_E_

# T -> FT'
class T(Non_Term):
    def __init__(self, name, value):
        super().__init__(name, value)

    def walk_arithmetic(self, inh=None):
        val_F = self.interiors[0].walk_arithmetic()
        val_T_ = self.interiors[1].walk_arithmetic(val_F)
        return val_T_

# T' -> *FT' | e
class T_(Non_Term):
    def __init__(self, name, value):
        super().__init__(name, value)

    def walk_arithmetic(self, inh=None):
        if not self.leaves and not self.interiors:
            return inh
        val_F = self.interiors[0].walk_arithmetic()
        val_T_ = self.interiors[1].walk_arithmetic(inh * val_F)
        return val_T_

# F -> num | (E)
class F(Non_Term):
    def __init__(self, name, value):
        super().__init__(name, value)

    def walk_arithmetic(self, inh=None):
        if self.leaves[0].name == TERM.NUM.name:
            return self.leaves[0].attr
        return self.interiors[0].walk_arithmetic()

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

        self.end_sym = Token.gen("$")
        self.root = Non_Term.gen(NTERM.E)

        self.stack = Stack()
        self.stack.push(self.end_sym)
        self.stack.push(self.root)

    def predictive(self):
        self.curr = self.stack.top()
        self.prev = self.curr
        self.a = self.token_stream.get_next_token()
        while self.curr.name != self.end_sym.name:

            if self.curr.name == self.a.name:
                self.stack.pop()
                self.prev.append_leaf(self.a)
                self.a = self.token_stream.get_next_token()
            elif isinstance(self.curr, Token):
                raise ValueError("Un token no debería llegar hasta aquí. X: name=%s value=%d attr=%s" % (self.curr.name, self.curr.value, self.curr.attr))
            elif not self.ptable[self.curr.value][self.a.value]:
                raise ValueError("No hay entrada para X = %s (%d), a = %s (%d)" % (self.curr.name, self.curr.value, self.a.name, self.a.value))
            else:
                production = self.ptable[self.curr.value][self.a.value]
                self.creatnreplace_ints(production)
                self.append_ints(production)
                self.stack.pop()
                self.push_production(production)

            self.prev = self.curr
            self.curr = self.stack.top()
        return self.root

    def append_ints(self, production):
        for i in range(len(production)):
            g_sym = production[i]
            if isinstance(g_sym, TERM):
                continue
            self.curr.append_interior(g_sym)

    def creatnreplace_ints(self, production):
        for i in range(len(production)):
            g_sym = production[i]
            if isinstance(g_sym, TERM):
                continue
            interior = Non_Term.gen(g_sym)
            production[i] = interior

    def push_production(self, production):
        if production[0].name == TERM.EMPTY.name:
            return
        for i in range(len(production) - 1, -1, -1):
            g_sym = production[i]
            self.stack.push(g_sym)

if __name__ == "__main__":
    #inp = input()
    inp = "(7+3)*4"
    token_stream = Token_Stream(inp)
    parser = Parser(token_stream)
    parsetree = parser.predictive()
    res = parsetree.walk_arithmetic()
    print(res)
