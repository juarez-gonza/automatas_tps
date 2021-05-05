# ===================== NON-TERMINALS =====================

from grammar_symbols import *
class Non_Term(Grammar_Symbol):
    def __init__(self, name, value):
        self.leaves = []
        self.interiors = []
        super().__init__(name, value)

    def append_interior(self, childnode):
        self.interiors.append(childnode)

    def append_leaf(self, childnode):
        self.leaves.append(childnode)

    def walk_arithmetic(self, inh=None):
        pass

    @staticmethod
    def gen(nterm):
        if nterm.name == NTERM.E.name:
            return E(nterm.name, nterm.value)
        elif nterm.name == NTERM.E_.name:
            return E_(nterm.name, nterm.value)
        elif nterm.name == NTERM.T.name:
            return T(nterm.name, nterm.value)
        elif nterm.name == NTERM.T_.name:
            return T_(nterm.name, nterm.value)
        elif nterm.name == NTERM.F.name:
            return F(nterm.name, nterm.value)
        else:
            raise ValueError("Cannot generate non terminal @ Non_Term.gen(), no match for nterm")

# E  -> TE'
class E(Non_Term):
    def __init__(self, name, value):
        super().__init__(name, value)

    def walk_arithmetic(self, inh=None):
        val_T = self.interiors[0].walk_arithmetic()
        val_E_ = self.interiors[1].walk_arithmetic(val_T)
        return val_E_

# E' -> +TE | e
class E_(Non_Term):
    def __init__(self, name, value):
        super().__init__(name, value)

    def walk_arithmetic(self, inh=None):
        if not self.interiors:
            return inh
        val_T = self.interiors[0].walk_arithmetic()
        val_E_ = self.interiors[1].walk_arithmetic(inh + val_T)
        return val_E_

# T -> FT'
class T(Non_Term):
    def __init__(self, name, value):
        super().__init__(name, value)

    def walk_arithmetic(self, inh=None):
        val_F = self.interiors[0].walk_arithmetic()
        val_T_ = self.interiors[1].walk_arithmetic(val_F)
        return val_T_

# T' -> *FT' | e
class T_(Non_Term):
    def __init__(self, name, value):
        super().__init__(name, value)

    def walk_arithmetic(self, inh=None):
        if not self.leaves and not self.interiors:
            return inh
        val_F = self.interiors[0].walk_arithmetic()
        val_T_ = self.interiors[1].walk_arithmetic(inh * val_F)
        return val_T_

# F -> num | (E)
class F(Non_Term):
    def __init__(self, name, value):
        super().__init__(name, value)

    def walk_arithmetic(self, inh=None):
        if self.leaves[0].name == TERM.NUM.name:
            return self.leaves[0].attr
        return self.interiors[0].walk_arithmetic()
