from ll1_predictive import *
from terminals import *

if __name__ == "__main__":
    inp = input()
    token_stream = Token_Stream(inp)
    parser = Parser(token_stream)
    parsetree = parser.predictive()
    res = parsetree.walk_arithmetic()
    print(res)
