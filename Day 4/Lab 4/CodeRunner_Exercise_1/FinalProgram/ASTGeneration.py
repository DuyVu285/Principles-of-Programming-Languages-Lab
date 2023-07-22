from Exercise1Visitor import Exercise1Visitor
from Exercise1Parser import Exercise1Parser
from ASTUtils import *
from functools import reduce

class ASTGeneration(Exercise1Visitor):
    def visitProgram(self, ctx:Exercise1Parser.ProgramContext):
         return Prog([expr.accept(self) for expr in ctx.expression()])

    def visitExpression(self, ctx:Exercise1Parser.ExpressionContext):
        if ctx.expression():
            sign = ""
            if ctx.Add():
                sign = "+"
            elif ctx.Sub():
                sign = "-"
            
            return BinOp(sign, ctx.expression().accept(self), ctx.term().accept(self))
        else:
            return ctx.term().accept(self)

    def visitTerm(self, ctx:Exercise1Parser.TermContext):
        if ctx.term():
            sign = ""
            if ctx.Mul():
                sign = "*"
            elif ctx.Div():
                sign = "/"
            elif ctx.Mod():
                sign = "%"
            
            return BinOp(sign, ctx.term().accept(self), ctx.factor().accept(self))
        else:
            return ctx.factor().accept(self)

    def visitFactor(self, ctx:Exercise1Parser.FactorContext):
        if ctx.intTerm():
            return ctx.intTerm().accept(self)
    
    def visitIntTerm(self, ctx:Exercise1Parser.IntTermContext):
        return self.visitInteger(ctx.Integer())

    def visitInteger(self, node:Exercise1Parser.Integer):
        return Int(int(node.getText()))