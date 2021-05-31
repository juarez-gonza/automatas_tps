from enum import Enum
from Turing import *
from Report import *
from Input import *
from falsemain import *

# Expresión regular: (x|yx)*

class Estados(Enum):
    A = 0
    B = 1

    @staticmethod
    def get_init_st():
        return Estados.A

    @staticmethod
    def isfinal(st):
        fstates = [Estados.A.name]
        if st.name in fstates:
            return True
        return False

class Alfabeto(Enum):
    x = 0
    y = 1
    B_ = 2

    @staticmethod
    def get_alpha(c):
        if c == Alfabeto.x.name:
            return Alfabeto.x
        if c == Alfabeto.y.name:
            return Alfabeto.y
        raise ValueError("Caracter no presente en el alfabeto")

#                   x = 0           y = 1           B_ = 2
#           [
# A = 0         [[A, B_, R],         [B, B_, R]     [A, B_, L] <-- Estado final ]
# B = 1         [[A, B_, R],         []             []]
#           ]

tb = [
        [Transition(Estados.A, Alfabeto.B_, Direccion.R), Transition(Estados.B, Alfabeto.B_, Direccion.R), Transition(Estados.A, Alfabeto.B_, Direccion.L)],
        [Transition(Estados.A, Alfabeto.B_, Direccion.R), None, None]
]

if __name__ == "__main__":
    reporter = RPrinter()
    input_m = CLI_Input()
    t = Turing(tb, Estados, Alfabeto, reporter)
    fmain(t, reporter, input_m)
