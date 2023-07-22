# Generated from Exercise2.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .Exercise2Parser import Exercise2Parser
else:
    from Exercise2Parser import Exercise2Parser

# This class defines a complete generic visitor for a parse tree produced by Exercise2Parser.

class Exercise2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Exercise2Parser#intTerm.
    def visitIntTerm(self, ctx:Exercise2Parser.IntTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercise2Parser#factor.
    def visitFactor(self, ctx:Exercise2Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercise2Parser#term.
    def visitTerm(self, ctx:Exercise2Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercise2Parser#expression.
    def visitExpression(self, ctx:Exercise2Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercise2Parser#program.
    def visitProgram(self, ctx:Exercise2Parser.ProgramContext):
        return self.visitChildren(ctx)



del Exercise2Parser