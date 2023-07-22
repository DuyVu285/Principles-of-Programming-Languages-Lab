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
        4,1,11,37,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,
        1,1,2,1,2,1,2,1,2,1,2,3,2,20,8,2,1,3,1,3,1,3,1,3,1,3,3,3,27,8,3,
        1,4,5,4,30,8,4,10,4,12,4,33,9,4,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,2,
        1,0,3,5,1,0,1,2,34,0,10,1,0,0,0,2,12,1,0,0,0,4,19,1,0,0,0,6,26,1,
        0,0,0,8,31,1,0,0,0,10,11,5,6,0,0,11,1,1,0,0,0,12,13,3,0,0,0,13,3,
        1,0,0,0,14,15,3,2,1,0,15,16,7,0,0,0,16,17,3,4,2,0,17,20,1,0,0,0,
        18,20,3,2,1,0,19,14,1,0,0,0,19,18,1,0,0,0,20,5,1,0,0,0,21,22,3,4,
        2,0,22,23,7,1,0,0,23,24,3,6,3,0,24,27,1,0,0,0,25,27,3,4,2,0,26,21,
        1,0,0,0,26,25,1,0,0,0,27,7,1,0,0,0,28,30,3,6,3,0,29,28,1,0,0,0,30,
        33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,31,1,0,0,
        0,34,35,5,0,0,1,35,9,1,0,0,0,3,19,26,31
    ]

class Exercise2Parser ( Parser ):

    grammarFileName = "Exercise2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "Add", "Sub", "Mul", "Div", "Mod", "Integer", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_intTerm = 0
    RULE_factor = 1
    RULE_term = 2
    RULE_expression = 3
    RULE_program = 4

    ruleNames =  [ "intTerm", "factor", "term", "expression", "program" ]

    EOF = Token.EOF
    Add=1
    Sub=2
    Mul=3
    Div=4
    Mod=5
    Integer=6
    WS=7
    ERROR_CHAR=8
    UNCLOSE_STRING=9
    ILLEGAL_ESCAPE=10
    UNTERMINATED_COMMENT=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class IntTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self):
            return self.getToken(Exercise2Parser.Integer, 0)

        def getRuleIndex(self):
            return Exercise2Parser.RULE_intTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntTerm" ):
                return visitor.visitIntTerm(self)
            else:
                return visitor.visitChildren(self)




    def intTerm(self):

        localctx = Exercise2Parser.IntTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_intTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(Exercise2Parser.Integer)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intTerm(self):
            return self.getTypedRuleContext(Exercise2Parser.IntTermContext,0)


        def getRuleIndex(self):
            return Exercise2Parser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = Exercise2Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.intTerm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(Exercise2Parser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(Exercise2Parser.TermContext,0)


        def Mul(self):
            return self.getToken(Exercise2Parser.Mul, 0)

        def Div(self):
            return self.getToken(Exercise2Parser.Div, 0)

        def Mod(self):
            return self.getToken(Exercise2Parser.Mod, 0)

        def getRuleIndex(self):
            return Exercise2Parser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = Exercise2Parser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.factor()
                self.state = 15
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 16
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(Exercise2Parser.TermContext,0)


        def expression(self):
            return self.getTypedRuleContext(Exercise2Parser.ExpressionContext,0)


        def Add(self):
            return self.getToken(Exercise2Parser.Add, 0)

        def Sub(self):
            return self.getToken(Exercise2Parser.Sub, 0)

        def getRuleIndex(self):
            return Exercise2Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = Exercise2Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.term()
                self.state = 22
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 23
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Exercise2Parser.EOF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercise2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Exercise2Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return Exercise2Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = Exercise2Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 28
                self.expression()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(Exercise2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





