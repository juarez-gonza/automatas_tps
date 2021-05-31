from enum import Enum
from Turing import *
from Report import *
from Input import *
from falsemain import *

# Expresión regular: a*b|a

class Estados(Enum):
    A = 0
    B = 1
    C = 2
    D = 3

    @staticmethod
    def get_init_st():
        return Estados.A

    @staticmethod
    def isfinal(st):
        fstates = [Estados.B.name, Estados.C.name]
        if st.name in fstates:
            return True
        return False

class Alfabeto(Enum):
    a = 0
    b = 1
    B_ = 2

    @staticmethod
    def get_alpha(c):
        if c == Alfabeto.a.name:
            return Alfabeto.a
        if c == Alfabeto.b.name:
            return Alfabeto.b
        raise ValueError('Caracter no presente en el alfabeto')

#                   a = 0           b = 1           B_ = 2
#           [
# A = 0         [[B, B_, R],         [C, B_, R]     []]
# B = 1         [[D, B_, R],         [C, B_, R]     [B, B_, L] <-- Estado final ]
# C = 2         [[],                 []             [C, B_, L] <-- Estado final ]
# D = 3         [[D, B_, R],         [C, B_, R]     []]
#           ]

tb = [
        [Transition(Estados.B, Alfabeto.B_, Direccion.R), Transition(Estados.C, Alfabeto.B_, Direccion.R), None],
        [Transition(Estados.D, Alfabeto.B_, Direccion.R), Transition(Estados.C, Alfabeto.B_, Direccion.R), Transition(Estados.B, Alfabeto.B_, Direccion.L)],
        [None, None, Transition(Estados.C, Alfabeto.B_, Direccion.L)],
        [Transition(Estados.D, Alfabeto.B_, Direccion.R), Transition(Estados.C, Alfabeto.B_, Direccion.R), None],
]

if __name__ == '__main__':
    reporter = RPrinter()
    input_m = CLI_Input()
    t = Turing(tb, Estados, Alfabeto, reporter)
    fmain(t, reporter, input_m)
