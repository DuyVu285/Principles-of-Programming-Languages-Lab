from Exercise2Visitor import Exercise2Visitor
from Exercise2Parser import Exercise2Parser
from ASTUtils import *
from functools import reduce

class ASTGeneration(Exercise2Visitor):
    def visitProgram(self, ctx:Exercise2Parser.ProgramContext):
         return Prog([expr.accept(self) for expr in ctx.expression()])

    def visitExpression(self, ctx:Exercise2Parser.ExpressionContext):
        if ctx.expression():
            sign = ""
            if ctx.Add():
                sign = "+"
            elif ctx.Sub():
                sign = "-"
            
            return BinOp(sign, ctx.term().accept(self), ctx.expression().accept(self))
        else:
            return ctx.term().accept(self)

    def visitTerm(self, ctx:Exercise2Parser.TermContext):
        if ctx.term():
            sign = ""
            if ctx.Mul():
                sign = "*"
            elif ctx.Div():
                sign = "/"
            elif ctx.Mod():
                sign = "%"
            
            return BinOp(sign, ctx.factor().accept(self), ctx.term().accept(self))
        else:
            return ctx.factor().accept(self)

    def visitFactor(self, ctx:Exercise2Parser.FactorContext):
        if ctx.intTerm():
            return ctx.intTerm().accept(self)
    
    def visitIntTerm(self, ctx:Exercise2Parser.IntTermContext):
        return self.visitInteger(ctx.Integer())

    def visitInteger(self, node:Exercise2Parser.Integer):
        return Int(int(node.getText()))