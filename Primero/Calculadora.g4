grammar Calculadora;

programa:   instruccion+ ;
instruccion:   expresion NUEVA_LINEA      # imprimirExpr
    |   NUEVA_LINEA                       # vacio
    ;

expresion
    : <assoc=right> expresion '^' expresion   # PotenciaDerecha
    | expresion ('*'|'/') expresion           # MultiplicacionDivision
    | expresion ('+'|'-') expresion           # SumaResta
    | '-' expresion                           # Negativo
    | ENTERO                                  # Numero
    | '(' expresion ')'                       # Parentesis
    ;

NUEVA_LINEA: [\r\n]+ ;
ENTERO:    [0-9]+ ;
ESPACIO:   [ \t]+ -> skip ;

