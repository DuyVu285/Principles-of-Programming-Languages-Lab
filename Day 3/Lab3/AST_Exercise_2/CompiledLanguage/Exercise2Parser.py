# Generated from Exercise2.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,24,2,0,7,0,2,1,7,1,1,0,5,0,6,8,0,10,0,12,0,9,9,0,1,0,1,0,
        1,1,1,1,1,1,1,1,5,1,17,8,1,10,1,12,1,20,9,1,1,1,1,1,1,1,0,0,2,0,
        2,0,1,1,0,3,4,23,0,7,1,0,0,0,2,12,1,0,0,0,4,6,3,2,1,0,5,4,1,0,0,
        0,6,9,1,0,0,0,7,5,1,0,0,0,7,8,1,0,0,0,8,10,1,0,0,0,9,7,1,0,0,0,10,
        11,5,0,0,1,11,1,1,0,0,0,12,13,7,0,0,0,13,18,5,5,0,0,14,15,5,1,0,
        0,15,17,5,5,0,0,16,14,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,18,19,
        1,0,0,0,19,21,1,0,0,0,20,18,1,0,0,0,21,22,5,2,0,0,22,3,1,0,0,0,2,
        7,18
    ]

class Exercise2Parser ( Parser ):

    grammarFileName = "Exercise2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "';'", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "IntType", 
                      "FloatType", "Identifier", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1

    ruleNames =  [ "program", "statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    IntType=3
    FloatType=4
    Identifier=5
    WS=6
    ERROR_CHAR=7
    UNCLOSE_STRING=8
    ILLEGAL_ESCAPE=9
    UNTERMINATED_COMMENT=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Exercise2Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercise2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Exercise2Parser.StatementContext,i)


        def getRuleIndex(self):
            return Exercise2Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = Exercise2Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 4
                self.statement()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
            self.match(Exercise2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(Exercise2Parser.Identifier)
            else:
                return self.getToken(Exercise2Parser.Identifier, i)

        def IntType(self):
            return self.getToken(Exercise2Parser.IntType, 0)

        def FloatType(self):
            return self.getToken(Exercise2Parser.FloatType, 0)

        def getRuleIndex(self):
            return Exercise2Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = Exercise2Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 13
            self.match(Exercise2Parser.Identifier)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 14
                self.match(Exercise2Parser.T__0)
                self.state = 15
                self.match(Exercise2Parser.Identifier)
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 21
            self.match(Exercise2Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





