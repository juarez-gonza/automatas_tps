from enum import Enum
from Turing import *
from Report import *
from Input import *
from falsemain import *

# Expresión regular: a*|ba

class Estado(Enum):
    A = 0
    B = 1
    C = 2
    D = 3

    @staticmethod
    def get_init_st():
        return Estado.A

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
        raise ValueError("Caracter no presente en el alfabeto")

#                   a = 0           b = 1           B_ = 2
#           [
# A = 0         [[B, B_, R],         [C, B_, R]     [A, B_, L] <-- Estado final ]
# B = 1         [[B, B_, R],         []             [B, B_, L] <-- Estado final ]
# C = 2         [[D, B_, R],         []             []]
# D = 3         [[],                 []             [D, B_, L] <-- Estado final ]
#           ]

tb = [
        [Transition(Estado.B, Alfabeto.B_, Direccion.R), Transition(Estado.C, Alfabeto.B_, Direccion.R), Transition(Estado.A, Alfabeto.B_, Direccion.L, True)],
        [Transition(Estado.B, Alfabeto.B_, Direccion.R), None, Transition(Estado.B, Alfabeto.B_, Direccion.L, True)],
        [Transition(Estado.D, Alfabeto.B_, Direccion.R), None, None],
        [None, None, Transition(Estado.D, Alfabeto.B_, Direccion.L, True)]
]

if __name__ == "__main__":
    reporter = RPrinter()
    input_m = CLI_Input()
    t = Turing(tb, Estado.get_init_st(), Alfabeto, reporter)
    fmain(t, reporter, input_m)
