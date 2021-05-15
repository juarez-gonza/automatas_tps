from enum import Enum

class Direccion(Enum):
    L = 0
    R = 1

class Transition():
    def __init__(self, nxt_st, nxt_alpha, nxt_dir):
        self.nxt_st = nxt_st
        self.nxt_alpha = nxt_alpha
        self.nxt_dir = nxt_dir

    def get_nxt_st(self):
        return self.nxt_st

    def get_nxt_alpha(self):
        return self.nxt_alpha

    def get_nxt_dir(self):
        return self.nxt_dir

class Turing():
    def __init__(self, tb, init_st, alfabeto, report):
        self.tb = tb
        self.tape = []
        self.th = 0
        self.st = init_st
        self.alfabeto = alfabeto
        self.report = report

    def init_tape(self, string):
        self.tape = [self.alfabeto.get_alpha(c) for c in string] + [self.alfabeto.B_]

    def run(self):
        curr = self.tape[self.th]
        ok = True

        while True:

            tr = self.tb[self.st.value][curr.value]
            if not tr:
                ok = False
                self.report.summit(self.st.name, curr.name, "/")
                break

            nxt_st = tr.get_nxt_st()
            nxt_alpha = tr.get_nxt_alpha()
            nxt_dir = tr.get_nxt_dir()

            self.report.summit(self.st.name, curr.name, nxt_st.name)

            self.st = nxt_st
            self.tape[self.th] = nxt_alpha

            if nxt_dir == Direccion.L:
                self.th -= 1
            else:
                self.th += 1

            curr = self.tape[self.th]

            # Si fuera la condición de while loop la cadena vacía siempre se aceptaría
            # que solo es el caso para regex de la forma (x)*
            if curr == self.alfabeto.B_:
                break

        self.report.gen_log(ok)
