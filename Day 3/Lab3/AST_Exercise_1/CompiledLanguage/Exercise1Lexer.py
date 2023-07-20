# Generated from Exercise1.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,11,56,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,2,1,2,
        1,3,1,3,1,4,4,4,33,8,4,11,4,12,4,34,1,5,4,5,38,8,5,11,5,12,5,39,
        1,6,4,6,43,8,6,11,6,12,6,44,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,
        1,10,0,0,11,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,
        1,0,3,1,0,48,57,1,0,97,122,3,0,9,10,13,13,32,32,58,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,
        1,0,0,0,3,25,1,0,0,0,5,27,1,0,0,0,7,29,1,0,0,0,9,32,1,0,0,0,11,37,
        1,0,0,0,13,42,1,0,0,0,15,48,1,0,0,0,17,50,1,0,0,0,19,52,1,0,0,0,
        21,54,1,0,0,0,23,24,5,43,0,0,24,2,1,0,0,0,25,26,5,45,0,0,26,4,1,
        0,0,0,27,28,5,42,0,0,28,6,1,0,0,0,29,30,5,47,0,0,30,8,1,0,0,0,31,
        33,7,0,0,0,32,31,1,0,0,0,33,34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,
        0,35,10,1,0,0,0,36,38,7,1,0,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,
        1,0,0,0,39,40,1,0,0,0,40,12,1,0,0,0,41,43,7,2,0,0,42,41,1,0,0,0,
        43,44,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,46,1,0,0,0,46,47,6,
        6,0,0,47,14,1,0,0,0,48,49,9,0,0,0,49,16,1,0,0,0,50,51,9,0,0,0,51,
        18,1,0,0,0,52,53,9,0,0,0,53,20,1,0,0,0,54,55,9,0,0,0,55,22,1,0,0,
        0,4,0,34,39,44,1,6,0,0
    ]

class Exercise1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Add = 1
    Sub = 2
    Mul = 3
    Div = 4
    Integer = 5
    Identifier = 6
    WS = 7
    ERROR_CHAR = 8
    UNCLOSE_STRING = 9
    ILLEGAL_ESCAPE = 10
    UNTERMINATED_COMMENT = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "Add", "Sub", "Mul", "Div", "Integer", "Identifier", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "Add", "Sub", "Mul", "Div", "Integer", "Identifier", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "Exercise1.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


