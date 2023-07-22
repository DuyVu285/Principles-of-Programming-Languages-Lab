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
        4,1,11,45,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,
        1,1,2,1,2,1,2,1,2,1,2,1,2,5,2,21,8,2,10,2,12,2,24,9,2,1,3,1,3,1,
        3,1,3,1,3,1,3,5,3,32,8,3,10,3,12,3,35,9,3,1,4,5,4,38,8,4,10,4,12,
        4,41,9,4,1,4,1,4,1,4,0,2,4,6,5,0,2,4,6,8,0,2,1,0,3,5,1,0,1,2,42,
        0,10,1,0,0,0,2,12,1,0,0,0,4,14,1,0,0,0,6,25,1,0,0,0,8,39,1,0,0,0,
        10,11,5,6,0,0,11,1,1,0,0,0,12,13,3,0,0,0,13,3,1,0,0,0,14,15,6,2,
        -1,0,15,16,3,2,1,0,16,22,1,0,0,0,17,18,10,2,0,0,18,19,7,0,0,0,19,
        21,3,2,1,0,20,17,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,
        0,23,5,1,0,0,0,24,22,1,0,0,0,25,26,6,3,-1,0,26,27,3,4,2,0,27,33,
        1,0,0,0,28,29,10,2,0,0,29,30,7,1,0,0,30,32,3,4,2,0,31,28,1,0,0,0,
        32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,7,1,0,0,0,35,33,1,0,
        0,0,36,38,3,6,3,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,
        1,0,0,0,40,42,1,0,0,0,41,39,1,0,0,0,42,43,5,0,0,1,43,9,1,0,0,0,3,
        22,33,39
    ]

class Exercise1Parser ( Parser ):

    grammarFileName = "Exercise1.g4"

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
            return self.getToken(Exercise1Parser.Integer, 0)

        def getRuleIndex(self):
            return Exercise1Parser.RULE_intTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntTerm" ):
                return visitor.visitIntTerm(self)
            else:
                return visitor.visitChildren(self)




    def intTerm(self):

        localctx = Exercise1Parser.IntTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_intTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(Exercise1Parser.Integer)
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
            return self.getTypedRuleContext(Exercise1Parser.IntTermContext,0)


        def getRuleIndex(self):
            return Exercise1Parser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = Exercise1Parser.FactorContext(self, self._ctx, self.state)
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
            return self.getTypedRuleContext(Exercise1Parser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(Exercise1Parser.TermContext,0)


        def Mul(self):
            return self.getToken(Exercise1Parser.Mul, 0)

        def Div(self):
            return self.getToken(Exercise1Parser.Div, 0)

        def Mod(self):
            return self.getToken(Exercise1Parser.Mod, 0)

        def getRuleIndex(self):
            return Exercise1Parser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Exercise1Parser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 22
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Exercise1Parser.TermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 17
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 18
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 19
                    self.factor() 
                self.state = 24
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(Exercise1Parser.TermContext,0)


        def expression(self):
            return self.getTypedRuleContext(Exercise1Parser.ExpressionContext,0)


        def Add(self):
            return self.getToken(Exercise1Parser.Add, 0)

        def Sub(self):
            return self.getToken(Exercise1Parser.Sub, 0)

        def getRuleIndex(self):
            return Exercise1Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Exercise1Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Exercise1Parser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 28
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 29
                    _la = self._input.LA(1)
                    if not(_la==1 or _la==2):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 30
                    self.term(0) 
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Exercise1Parser.EOF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exercise1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Exercise1Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return Exercise1Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = Exercise1Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 36
                self.expression(0)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(Exercise1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.term_sempred
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




