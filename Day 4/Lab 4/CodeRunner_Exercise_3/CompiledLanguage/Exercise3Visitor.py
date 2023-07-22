# Generated from Exercise3.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .Exercise3Parser import Exercise3Parser
else:
    from Exercise3Parser import Exercise3Parser

# This class defines a complete generic visitor for a parse tree produced by Exercise3Parser.

class Exercise3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Exercise3Parser#intTerm.
    def visitIntTerm(self, ctx:Exercise3Parser.IntTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercise3Parser#factor.
    def visitFactor(self, ctx:Exercise3Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercise3Parser#term.
    def visitTerm(self, ctx:Exercise3Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercise3Parser#expression.
    def visitExpression(self, ctx:Exercise3Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Exercise3Parser#program.
    def visitProgram(self, ctx:Exercise3Parser.ProgramContext):
        return self.visitChildren(ctx)



del Exercise3Parser