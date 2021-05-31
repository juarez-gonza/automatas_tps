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
    def __init__(self, tb, estados, alfabeto, report):
        self.tb = tb
        self.tape = []
        self.th = 0
        self.estados = estados
        self.alfabeto = alfabeto
        self.report = report

    def init_tape(self, string):
        self.tape = [self.alfabeto.get_alpha(c) for c in string] + [self.alfabeto.B_]

    def run(self):
        curr_st = self.estados.get_init_st()
        curr_alpha = self.tape[self.th]
        status = True

        while True:

            tr = self.tb[curr_st.value][curr_alpha.value]
            if not tr:
                status = False
                self.report.summit(curr_st.name, curr_alpha.name, "/")
                break

            nxt_st = tr.get_nxt_st()
            nxt_alpha = tr.get_nxt_alpha()
            nxt_dir = tr.get_nxt_dir()

            self.report.summit(curr_st.name, curr_alpha.name, nxt_st.name)

            curr_st = nxt_st
            self.tape[self.th] = nxt_alpha

            if nxt_dir == Direccion.L:
                self.th -= 1
            else:
                self.th += 1

            curr_alpha = self.tape[self.th]

            # Si fuera la condición de while loop la cadena vacía siempre se aceptaría
            # que solo es el caso para regex de la forma (x)*
            if curr_st.isfinal(curr_st) and curr_alpha == self.alfabeto.B_:
                break

        self.report.set_status(status)

        return status
