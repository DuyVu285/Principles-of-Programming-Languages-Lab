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
        4,0,8,98,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,3,0,19,8,0,1,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,
        1,1,3,1,29,8,1,1,1,1,1,5,1,33,8,1,10,1,12,1,36,9,1,1,1,1,1,5,1,40,
        8,1,10,1,12,1,43,9,1,3,1,45,8,1,1,1,3,1,48,8,1,1,1,1,1,5,1,52,8,
        1,10,1,12,1,55,9,1,1,1,1,1,3,1,59,8,1,1,1,4,1,62,8,1,11,1,12,1,63,
        3,1,66,8,1,1,2,1,2,5,2,70,8,2,10,2,12,2,73,9,2,1,2,1,2,5,2,77,8,
        2,10,2,12,2,80,9,2,3,2,82,8,2,1,3,4,3,85,8,3,11,3,12,3,86,1,3,1,
        3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,
        13,7,15,8,1,0,6,2,0,43,43,45,45,1,0,49,57,1,0,48,57,2,0,69,69,101,
        101,1,0,48,49,3,0,9,10,13,13,32,32,112,0,1,1,0,0,0,0,3,1,0,0,0,0,
        5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,
        1,0,0,0,1,18,1,0,0,0,3,65,1,0,0,0,5,81,1,0,0,0,7,84,1,0,0,0,9,90,
        1,0,0,0,11,92,1,0,0,0,13,94,1,0,0,0,15,96,1,0,0,0,17,19,7,0,0,0,
        18,17,1,0,0,0,18,19,1,0,0,0,19,20,1,0,0,0,20,24,7,1,0,0,21,23,7,
        2,0,0,22,21,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,
        2,1,0,0,0,26,24,1,0,0,0,27,29,7,0,0,0,28,27,1,0,0,0,28,29,1,0,0,
        0,29,30,1,0,0,0,30,34,7,1,0,0,31,33,7,2,0,0,32,31,1,0,0,0,33,36,
        1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,44,1,0,0,0,36,34,1,0,0,0,
        37,41,5,46,0,0,38,40,7,2,0,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,
        0,0,0,41,42,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,44,37,1,0,0,0,44,
        45,1,0,0,0,45,66,1,0,0,0,46,48,7,0,0,0,47,46,1,0,0,0,47,48,1,0,0,
        0,48,49,1,0,0,0,49,53,7,1,0,0,50,52,7,2,0,0,51,50,1,0,0,0,52,55,
        1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,53,1,0,0,0,
        56,58,7,3,0,0,57,59,7,0,0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,61,1,
        0,0,0,60,62,7,2,0,0,61,60,1,0,0,0,62,63,1,0,0,0,63,61,1,0,0,0,63,
        64,1,0,0,0,64,66,1,0,0,0,65,28,1,0,0,0,65,47,1,0,0,0,66,4,1,0,0,
        0,67,71,5,48,0,0,68,70,7,4,0,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,
        1,0,0,0,71,72,1,0,0,0,72,82,1,0,0,0,73,71,1,0,0,0,74,78,5,49,0,0,
        75,77,7,4,0,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,
        0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,81,67,1,0,0,0,81,74,1,0,0,0,82,
        6,1,0,0,0,83,85,7,5,0,0,84,83,1,0,0,0,85,86,1,0,0,0,86,84,1,0,0,
        0,86,87,1,0,0,0,87,88,1,0,0,0,88,89,6,3,0,0,89,8,1,0,0,0,90,91,9,
        0,0,0,91,10,1,0,0,0,92,93,9,0,0,0,93,12,1,0,0,0,94,95,9,0,0,0,95,
        14,1,0,0,0,96,97,9,0,0,0,97,16,1,0,0,0,16,0,18,24,28,34,41,44,47,
        53,58,63,65,71,78,81,86,1,6,0,0
    ]

class Exercise1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    FLOAT = 2
    BINARY = 3
    WS = 4
    ERROR_CHAR = 5
    UNCLOSE_STRING = 6
    ILLEGAL_ESCAPE = 7
    UNTERMINATED_COMMENT = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "BINARY", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "INT", "FLOAT", "BINARY", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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


