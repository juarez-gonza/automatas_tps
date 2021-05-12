from ll1_predictive import *
from terminals import *

if __name__ == "__main__":
    print("\n\t=============== LL(1) Parser y analizador de sintaxis ===============\n")
    print("Las operaciones posibles son: adición (+) y multiplicación (*)")
    print("Se pueden usar paréntesis para forzar la precedencia. Ej.: (1+2)*4 = 3*4 = 12\n")
    inp = input("\tIngresar una operación aritmética: ")
    token_stream = Token_Stream(inp)
    parser = Parser(token_stream)
    parsetree = parser.predictive()
    res = parsetree.walk_arithmetic()
    print(res)
