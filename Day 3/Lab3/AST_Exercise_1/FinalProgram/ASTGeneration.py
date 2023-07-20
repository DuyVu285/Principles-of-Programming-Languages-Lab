from Exercise1Visitor import Exercise1Visitor
from Exercise1Parser import Exercise1Parser
from ASTUtils import *


class ASTGeneration(Exercise1Visitor):
    def visitProgram(self, ctx: Exercise1Parser.ProgramContext):
        expressions = [expression.accept(self) for expression in ctx.expression()]
        return Prog(expressions)

    def visitExpression(self, ctx: Exercise1Parser.ExpressionContext):
        if ctx.expression():
            if ctx.Add():
                return BinOp(
                    "+", ctx.expression().accept(self), ctx.factor().accept(self)
                )
            elif ctx.Sub():
                return BinOp(
                    "-", ctx.expression().accept(self), ctx.factor().accept(self)
                )
        else:
            return ctx.factor().accept(self)

    def visitFactor(self, ctx: Exercise1Parser.FactorContext):
        if ctx.factor():
            if ctx.Mul():
                return BinOp("*", ctx.factor().accept(self), ctx.term().accept(self))
            elif ctx.Div():
                return BinOp("/", ctx.factor().accept(self), ctx.term().accept(self))
        else:
            return ctx.term().accept(self)

    def visitTerm(self, ctx: Exercise1Parser.TermContext):
        if ctx.Integer():
            return self.visitInteger(ctx.Integer())
        elif ctx.Identifier():
            return self.visitIdentifier(ctx.Identifier())

    def visitInteger(self, node: Exercise1Parser.Integer):
        return Int()

    def visitIdentifier(self, node: Exercise1Parser.Identifier):
        return Id()
