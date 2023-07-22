# Generated from Exercise3.g4 by ANTLR 4.13.0
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
        4,1,11,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,
        1,1,1,3,1,16,8,1,1,2,1,2,1,2,1,2,1,2,3,2,23,8,2,1,3,1,3,1,3,1,3,
        1,3,3,3,30,8,3,1,4,5,4,33,8,4,10,4,12,4,36,9,4,1,4,1,4,1,4,0,0,5,
        0,2,4,6,8,0,2,1,0,3,5,1,0,1,2,38,0,10,1,0,0,0,2,15,1,0,0,0,4,22,
        1,0,0,0,6,29,1,0,0,0,8,34,1,0,0,0,10,11,5,6,0,0,11,1,1,0,0,0,12,
        16,3,0,0,0,13,14,5,2,0,0,14,16,3,0,0,0,15,12,1,0,0,0,15,13,1,0,0,
        0,16,3,1,0,0,0,17,18,3,2,1,0,18,19,7,0,0,0,19,20,3,4,2,0,20,23,1,
        0,0,0,21,23,3,2,1,0,22,17,1,0,0,0,22,21,1,0,0,0,23,5,1,0,0,0,24,
        25,3,4,2,0,25,26,7,1,0,0,26,27,3,6,3,0,27,30,1,0,0,0,28,30,3,4,2,
        0,29,24,1,0,0,0,29,28,1,0,0,0,30,7,1,0,0,0,31,33,3,6,3,0,32,31,1,
        0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,
        34,1,0,0,0,37,38,5,0,0,1,38,9,1,0,0,0,4,15,22,29,34
    ]

class Exercise3Parser ( Parser ):

    grammarFileName = "Exercise3.g4"

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
            return self.getToken(Exercise3Parser.Integer, 0)

        def getRuleIndex(self):
            return Exercise3Parser.RULE_intTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntTerm" ):
                return visitor.visitIntTerm(self)
            else:
                return visitor.visitChildren(self)




    def intTerm(self):

        localctx = Exercise3Parser.IntTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_intTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(Exercise3Parser.Integer)
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
            return self.getTypedRuleContext(Exercise3Parser.IntTermContext,0)


        def Sub(self):
            return self.getToken(Exercise3Parser.Sub, 0)

        def getRuleIndex(self):
            return Exercise3Parser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = Exercise3Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_factor)
        try:
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.intTerm()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.match(Exercise3Parser.Sub)
                self.state = 14
                self.intTerm()
                pass
            else:
                raise NoViableAltException(self)

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
            return self.getTypedRuleContext(Exercise3Parser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(Exercise3Parser.TermContext,0)


        def Mul(self):
            return self.getToken(Exercise3Parser.Mul, 0)

        def Div(self):
            return self.getToken(Exercise3Parser.Div, 0)

        def Mod(self):
            return self.getToken(Exercise3Parser.Mod, 0)

        def getRuleIndex(self):
            return Exercise3Parser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = Exercise3Parser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.factor()
                self.state = 18
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 19
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
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
            return self.getTypedRuleContext(Exercise3Parser.TermContext,0)


        def expression(self):
            return self.getTypedRuleContext(Exercise3Parser.ExpressionContext,0)


        def Add(self):
            return self.getToken(Exercise3Parser.Add, 0)

        def Sub(self):
            return self.getToken(Exercise3Parser.Sub, 0)

        def getRuleIndex(self):
            return Exercise3Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = Exercise3Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.term()
                self.state = 25
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 26
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
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
            return self.getToken(Exercise3Parser.EOF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercise3Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Exercise3Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return Exercise3Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = Exercise3Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==6:
                self.state = 31
                self.expression()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.match(Exercise3Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





