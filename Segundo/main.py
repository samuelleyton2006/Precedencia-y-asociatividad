import sys
from antlr4 import *
from ExprModifiedLexer import ExprModifiedLexer
from ExprModifiedParser import ExprModifiedParser
from EvalVisitorModified import EvalVisitorModified

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
        lexer = ExprModifiedLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ExprModifiedParser(stream)
        tree = parser.prog()

        visitor = EvalVisitorModified()
        result = visitor.visit(tree)

        print(f"Expr: {t}")
        print(f"ParseTree: {tree.toStringTree(recog=parser)}")
        print(f"Result: {result}")
        print("----")

if __name__ == '__main__':
    main()
