# Generated from Exercise1.g4 by ANTLR 4.13.0
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
        4,1,8,11,2,0,7,0,1,0,5,0,4,8,0,10,0,12,0,7,9,0,1,0,1,0,1,0,0,0,1,
        0,0,1,1,0,1,3,10,0,5,1,0,0,0,2,4,7,0,0,0,3,2,1,0,0,0,4,7,1,0,0,0,
        5,3,1,0,0,0,5,6,1,0,0,0,6,8,1,0,0,0,7,5,1,0,0,0,8,9,5,0,0,1,9,1,
        1,0,0,0,1,5
    ]

class Exercise1Parser ( Parser ):

    grammarFileName = "Exercise1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "BINARY", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    BINARY=3
    WS=4
    ERROR_CHAR=5
    UNCLOSE_STRING=6
    ILLEGAL_ESCAPE=7
    UNTERMINATED_COMMENT=8

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
            return self.getToken(Exercise1Parser.EOF, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(Exercise1Parser.INT)
            else:
                return self.getToken(Exercise1Parser.INT, i)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(Exercise1Parser.FLOAT)
            else:
                return self.getToken(Exercise1Parser.FLOAT, i)

        def BINARY(self, i:int=None):
            if i is None:
                return self.getTokens(Exercise1Parser.BINARY)
            else:
                return self.getToken(Exercise1Parser.BINARY, i)

        def getRuleIndex(self):
            return Exercise1Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = Exercise1Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 2
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 7
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 8
            self.match(Exercise1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





