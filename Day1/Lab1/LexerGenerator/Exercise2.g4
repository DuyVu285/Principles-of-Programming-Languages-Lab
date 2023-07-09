grammar Exercise2;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options{
	language=Python3;
}

program: (ID|INT|FLOAT|BINARY|OP)* EOF;

ID: [a-z][a-zA-Z0-9_]* ;
INT: ([+-])?[1-9][0-9]* ;
FLOAT: ([+-])?[1-9][0-9]*('.'[0-9]*)? | ([+-])?[1-9][0-9]*([eE][+-]?[0-9]+) ;
BINARY: '0'[01]* | '1'[01]* ;
OP: '+' | '-' | '*' | '/' | '%' ;

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;