import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitorOriginal import EvalVisitorOriginal

def main():
    tests = [
        "1+2*3",
        "10-5-2",
        "2^3^2",
        "4/2+3",
        "2-3*4",
        "(1+2)*3",
        "4/2*3"
    ]

    for t in tests:
        input_stream = InputStream(t)
        lexer = ExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()

        visitor = EvalVisitorOriginal()
        result = visitor.visit(tree)

        print(f"Expr: {t}")
        print(f"ParseTree: {tree.toStringTree(recog=parser)}")
        print(f"Result: {result}")
        print("----")

if __name__ == '__main__':
    main()
