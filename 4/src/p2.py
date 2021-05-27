from enum import Enum
from Turing import *
from Report import *
from Input import *
from falsemain import *

# Expresión regular: (x|yx)*

class Estado(Enum):
    A = 0
    B = 1

    @staticmethod
    def get_init_st():
        return Estado.A

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
        [Transition(Estado.A, Alfabeto.B_, Direccion.R), Transition(Estado.B, Alfabeto.B_, Direccion.R), Transition(Estado.A, Alfabeto.B_, Direccion.L, True)],
        [Transition(Estado.A, Alfabeto.B_, Direccion.R), None, None]
]

if __name__ == "__main__":
    reporter = RPrinter()
    input_m = CLI_Input()
    t = Turing(tb, Estado.get_init_st(), Alfabeto, reporter)
    fmain(t, reporter, input_m)
