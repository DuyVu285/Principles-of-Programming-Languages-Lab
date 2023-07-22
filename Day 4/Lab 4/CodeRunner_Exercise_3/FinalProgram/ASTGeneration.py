from Exercise3Visitor import Exercise3Visitor
from Exercise3Parser import Exercise3Parser
from ASTUtils import *
from functools import reduce

class ASTGeneration(Exercise3Visitor):
    def visitProgram(self, ctx:Exercise3Parser.ProgramContext):
         return Prog([expr.accept(self) for expr in ctx.expression()])

    def visitExpression(self, ctx:Exercise3Parser.ExpressionContext):
        if ctx.expression():
            sign = ""
            if ctx.Add():
                sign = "+"
            elif ctx.Sub():
                sign = "-"
            
            return BinOp(sign, ctx.term().accept(self), ctx.expression().accept(self))
        else:
            return ctx.term().accept(self)

    def visitTerm(self, ctx:Exercise3Parser.TermContext):
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

    def visitFactor(self, ctx:Exercise3Parser.FactorContext):
        if ctx.intTerm():
                if ctx.Sub():
                    sign = "-"
                    return BinOp(sign,Int(0), ctx.intTerm().accept(self))
                return ctx.intTerm().accept(self)
    
    def visitIntTerm(self, ctx:Exercise3Parser.IntTermContext):
        return self.visitInteger(ctx.Integer())

    def visitInteger(self, node:Exercise3Parser.Integer):
        return Int(int(node.getText()))