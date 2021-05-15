from enum import Enum
from Turing import *
from Report import *

class Estado(Enum):
    A = 0
    B = 1
    C = 2
    D = 3

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

#                   a = 0           b = 1           B_
#           [
# A = 0         [[B, B_, R],         [C, B_, R]     [A, B_, L] <-- Estado final ]
# B = 1         [[B, B_, R],         []             []]
# C = 2         [[D, B_, R],         []             []]
# D = 3         [[],                 []             [D, B_, L] <-- Estado final ]
#           ]

tb = [
        [Transition(Estado.B, Alfabeto.B_, Direccion.R), Transition(Estado.C, Alfabeto.B_, Direccion.R), Transition(Estado.A, Alfabeto.B_, Direccion.L)],
        [Transition(Estado.B, Alfabeto.B_, Direccion.R), None, None],
        [Transition(Estado.D, Alfabeto.B_, Direccion.R), None, None],
        [None, None, Transition(Estado.D, Alfabeto.B_, Direccion.L)]
]

if __name__ == "__main__":
    t = Turing(tb, Estado.A, Alfabeto, RPrinter())
    t.init_tape("ba")
    t.run()
