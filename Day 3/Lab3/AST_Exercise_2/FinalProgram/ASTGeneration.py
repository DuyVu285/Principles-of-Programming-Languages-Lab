from Exercise2Visitor import Exercise2Visitor
from Exercise2Parser import Exercise2Parser
from ASTUtils import *


class ASTGeneration(Exercise2Visitor):
    def visitProgram(self, ctx: Exercise2Parser.ProgramContext):
        statements = [statement.accept(self) for statement in ctx.statement()]
        return Prog(statements)

    def visitStatement(self, ctx: Exercise2Parser.StatementContext):
        identifiers = [token.getText() for token in ctx.Identifier()]
        if ctx.IntType():
            return IntStatement(identifiers)
        elif ctx.FloatType():
            return FloatStatement(identifiers)

    def visitIdentifier(self, node: Exercise2Parser.Identifier):
        return Id()

