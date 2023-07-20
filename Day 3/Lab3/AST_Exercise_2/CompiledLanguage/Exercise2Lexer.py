# Generated from Exercise2.g4 by ANTLR 4.13.0
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
        4,0,10,55,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,4,4,4,37,8,4,11,4,12,4,38,1,5,4,5,42,8,5,
        11,5,12,5,43,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,0,0,10,1,1,
        3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,1,0,2,1,0,97,122,3,0,9,
        10,13,13,32,32,56,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,
        0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,
        0,0,19,1,0,0,0,1,21,1,0,0,0,3,23,1,0,0,0,5,25,1,0,0,0,7,29,1,0,0,
        0,9,36,1,0,0,0,11,41,1,0,0,0,13,47,1,0,0,0,15,49,1,0,0,0,17,51,1,
        0,0,0,19,53,1,0,0,0,21,22,5,44,0,0,22,2,1,0,0,0,23,24,5,59,0,0,24,
        4,1,0,0,0,25,26,5,105,0,0,26,27,5,110,0,0,27,28,5,116,0,0,28,6,1,
        0,0,0,29,30,5,102,0,0,30,31,5,108,0,0,31,32,5,111,0,0,32,33,5,97,
        0,0,33,34,5,116,0,0,34,8,1,0,0,0,35,37,7,0,0,0,36,35,1,0,0,0,37,
        38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,10,1,0,0,0,40,42,7,1,0,
        0,41,40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,45,
        1,0,0,0,45,46,6,5,0,0,46,12,1,0,0,0,47,48,9,0,0,0,48,14,1,0,0,0,
        49,50,9,0,0,0,50,16,1,0,0,0,51,52,9,0,0,0,52,18,1,0,0,0,53,54,9,
        0,0,0,54,20,1,0,0,0,3,0,38,43,1,6,0,0
    ]

class Exercise2Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    IntType = 3
    FloatType = 4
    Identifier = 5
    WS = 6
    ERROR_CHAR = 7
    UNCLOSE_STRING = 8
    ILLEGAL_ESCAPE = 9
    UNTERMINATED_COMMENT = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "';'", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>",
            "IntType", "FloatType", "Identifier", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "IntType", "FloatType", "Identifier", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

    grammarFileName = "Exercise2.g4"

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


