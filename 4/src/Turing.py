from enum import Enum

class Direccion(Enum):
    L = 0
    R = 1

class Turing():
    def __init__(self, tb, init_st, alfabeto):
        self.tb = tb
        self.tape = []
        self.th = 0
        self.st = init_st
        self.alfabeto = alfabeto

    def init_tape(self, string):
        self.tape = [self.alfabeto.get_alpha(c) for c in string] + [self.alfabeto.B_]

    def run(self):
        curr = self.tape[self.th]

        while curr != self.alfabeto.B_:

            trans = self.tb[self.st.value][curr.value]
            if not trans:
                raise ValueError("No existe transición", self.st, curr)

            nxt_st = trans.get_nxt_st()
            nxt_alpha = trans.get_nxt_alpha()
            nxt_dir = trans.get_nxt_dir()


            self.st = nxt_st
            self.tape[self.th] = nxt_alpha

            if nxt_dir == Direccion.L:
                self.th -= 1
            else:
                self.th += 1
            print(self.tape)

            curr = self.tape[self.th]
