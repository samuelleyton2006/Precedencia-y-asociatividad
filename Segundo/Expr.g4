// ExprModified.g4 (Rediseñada: + mayor precedencia que *, y - es right-assoc)
grammar ExprModified;

prog: expr EOF ;

expr
    : <assoc=right> expr '^' expr         # Pow
    | expr op='+' expr                    # AddPlus
    | <assoc=right> expr op='-' expr      # SubRight
    | expr op=('*'|'/') expr              # MulDiv
    | INT                                 # Int
    | '(' expr ')'                        # Parens
    ;

INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
