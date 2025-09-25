from ExprVisitor import ExprVisitor
from ExprParser import ExprParser
import math

class EvalVisitorOriginal(ExprVisitor):

    def visitProg(self, ctx: ExprParser.ProgContext):
        return self.visit(ctx.expr())

    def visitInt(self, ctx: ExprParser.IntContext):
        return int(ctx.INT().getText())

    def visitParens(self, ctx: ExprParser.ParensContext):
        return self.visit(ctx.expr())

    def visitAddSub(self, ctx: ExprParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+':
            return left + right
        else:
            return left - right

    def visitMulDiv(self, ctx: ExprParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '*':
            return left * right
        else:
            return left / right

    def visitPow(self, ctx: ExprParser.PowContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return math.pow(left, right)
