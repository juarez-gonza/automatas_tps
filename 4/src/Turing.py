from enum import Enum

class Direccion(Enum):
    L = 0
    R = 1

class Turing():
    st_idx = 0
    char_idx = 1
    dir_idx = 2

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

            self.st = trans[Turing.st_idx]
            self.tape[self.th] = trans[Turing.char_idx]

            if trans[Turing.dir_idx] == Direccion.L:
                self.th -= 1
            else:
                self.th += 1
            print(self.tape)

            curr = self.tape[self.th]
