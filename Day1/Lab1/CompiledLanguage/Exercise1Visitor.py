# Generated from Exercise1.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .Exercise1Parser import Exercise1Parser
else:
    from Exercise1Parser import Exercise1Parser

# This class defines a complete generic visitor for a parse tree produced by Exercise1Parser.

class Exercise1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Exercise1Parser#program.
    def visitProgram(self, ctx:Exercise1Parser.ProgramContext):
        return self.visitChildren(ctx)



del Exercise1Parser