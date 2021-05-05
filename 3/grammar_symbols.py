import enum

# ===================== GRAMMAR-SYMBOL INTERFACE (== Enum interface) =====================
class Grammar_Symbol():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    @staticmethod
    def gen(g_sym):
        pass


# TERMINAL (INPUT SYMBOL)
class TERM(enum.Enum):
    NUM = 0
    SUM = 1
    MUL = 2
    O_PAREN = 3
    C_PAREN = 4
    END_SYM = 5
    EMPTY = 6

# NON-TERMINAL
class NTERM(enum.Enum):
    E = 0
    E_ = 1
    T = 2
    T_ = 3
    F = 4
