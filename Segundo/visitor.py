from ExprModifiedVisitor import ExprModifiedVisitor
from ExprModifiedParser import ExprModifiedParser
import math

class EvalVisitorModified(ExprModifiedVisitor):

    def visitProg(self, ctx: ExprModifiedParser.ProgContext):
        return self.visit(ctx.expr())

    def visitInt(self, ctx: ExprModifiedParser.IntContext):
        return int(ctx.INT().getText())

    def visitParens(self, ctx: ExprModifiedParser.ParensContext):
        return self.visit(ctx.expr())

    def visitAddPlus(self, ctx: ExprModifiedParser.AddPlusContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left + right

    def visitSubRight(self, ctx: ExprModifiedParser.SubRightContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left - right

    def visitMulDiv(self, ctx: ExprModifiedParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '*':
            return left * right
        else:
            return left / right

    def visitPow(self, ctx: ExprModifiedParser.PowContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return math.pow(left, right)
