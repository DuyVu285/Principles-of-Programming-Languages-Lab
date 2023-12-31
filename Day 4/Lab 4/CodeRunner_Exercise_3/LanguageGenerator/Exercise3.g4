grammar Exercise3;

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

intTerm: Integer;

factor
    : intTerm | Sub intTerm
    ;

term
    : factor (Mul | Div | Mod) term
    | factor
    ;

expression
    : term (Add | Sub) expression
    | term
    ;

program 
    : (expression)* EOF
    ;

Add : '+';
Sub : '-';
Mul : '*';
Div : '/';
Mod: '%';

Integer: [0-9]+ ;


WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;