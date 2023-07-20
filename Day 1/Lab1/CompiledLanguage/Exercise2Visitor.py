# Generated from Exercise2.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .Exercise2Parser import Exercise2Parser
else:
    from Exercise2Parser import Exercise2Parser

# This class defines a complete generic visitor for a parse tree produced by Exercise2Parser.

class Exercise2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Exercise2Parser#program.
    def visitProgram(self, ctx:Exercise2Parser.ProgramContext):
        return self.visitChildren(ctx)



del Exercise2Parser