from enum import Enum
from Turing import *

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

#                   a = 0           b = 1
#           [
# A = 0         [[B, B_, R],         [C, B_, R]]
# B = 1         [[B, B_, R],         []]
# C = 2         [[D, B_, R],         []]
# D = 3         [[],                 []]
#           ]

tb = [
        [Transition(Estado.B, Alfabeto.B_, Direccion.R), Transition(Estado.B, Alfabeto.B_, Direccion.R)],
        [Transition(Estado.B, Alfabeto.B_, Direccion.R), None],
        [Transition(Estado.D, Alfabeto.B_, Direccion.R), None],
        [None, None]
]

if __name__ == "__main__":
    t = Turing(tb, Estado.A, Alfabeto)
    t.init_tape("ba")
    t.run()
