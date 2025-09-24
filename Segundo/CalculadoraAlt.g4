grammar CalculadoraAlt;

programa:   instruccion+ ;
instruccion:   expresion NUEVA_LINEA      # imprimirExpr
    |   NUEVA_LINEA                       # vacio
    ;

// Cambiamos el orden: primero SumaResta, después MultiplicacionDivision
expresion
    : expresion ('+'|'-') expresion           # SumaResta
    | expresion ('*'|'/') expresion           # MultiplicacionDivision
    | expresion '^' expresion                 # PotenciaIzquierda
    | '-' expresion                           # Negativo
    | ENTERO                                  # Numero
    | '(' expresion ')'                       # Parentesis
    ;

NUEVA_LINEA: [\r\n]+ ;
ENTERO:    [0-9]+ ;
ESPACIO:   [ \t]+ -> skip ;

