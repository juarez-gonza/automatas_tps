from grammar_symbols import *
from nonterminals import *
from terminals import *
from stack import *

# Compilers: Principles, Techniques, & Tools - 2nd Edition
#       4.4.4: Nonrecursive Predictive Parsing


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
                self.prev.append_leaf(self.a)

                self.stack.pop()
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
