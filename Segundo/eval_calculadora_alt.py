# eval_calculadora_alt.py
import sys
from antlr4 import *
from CalculadoraAltLexer import CalculadoraAltLexer
from CalculadoraAltParser import CalculadoraAltParser
from CalculadoraAltVisitor import CalculadoraAltVisitor

class VisitanteCalculadoraAlt(CalculadoraAltVisitor):
    def visitImprimirExpr(self, ctx):
        return self.visit(ctx.expresion())

    def visitPotenciaIzquierda(self, ctx):
        izquierda = self.visit(ctx.expresion(0))
        derecha = self.visit(ctx.expresion(1))
        return izquierda ** derecha

    def visitMultiplicacionDivision(self, ctx):
        izquierda = self.visit(ctx.expresion(0))
        derecha = self.visit(ctx.expresion(1))
        op = ctx.getChild(1).getText()
        if op == '*':
            return izquierda * derecha
        else:
            return izquierda / derecha

    def visitSumaResta(self, ctx):
        izquierda = self.visit(ctx.expresion(0))
        derecha = self.visit(ctx.expresion(1))
        op = ctx.getChild(1).getText()
        if op == '+':
            return izquierda + derecha
        else:
            return izquierda - derecha

    def visitNegativo(self, ctx):
        return - self.visit(ctx.expresion())

    def visitNumero(self, ctx):
        return int(ctx.ENTERO().getText())

    def visitParentesis(self, ctx):
        return self.visit(ctx.expresion())

if __name__ == '__main__':
    datos = sys.stdin.read()
    flujo_entrada = InputStream(datos)
    analizador = CalculadoraAltLexer(flujo_entrada)
    flujo_tokens = CommonTokenStream(analizador)
    parser = CalculadoraAltParser(flujo_tokens)
    arbol = parser.programa()
    visitante = VisitanteCalculadoraAlt()
    for instr in arbol.instruccion():
        if instr.getChildCount() == 2:  # expresion NUEVA_LINEA
            valor = visitante.visit(instr.expresion())
            print(valor)
