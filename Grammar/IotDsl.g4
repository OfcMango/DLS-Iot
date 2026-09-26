grammar IoTDSL;

program
    : statement* EOF
    ;

statement
    : deviceDeclaration
    | deviceCommand
    | waitCommand
    | readCommand
    | ifStatement
    | loopStatement
    ;


/* Device declaration */

deviceDeclaration
    : DEVICE ID deviceType PIN NUMBER
    ;

deviceType
    : LED
    | TEMP
    | BUTTON
    ;


/* Device commands */

deviceCommand
    : ID (ON | OFF)
    ;


/* Wait */

waitCommand
    : WAIT NUMBER
    ;


/* Read */

readCommand
    : READ ID
    ;


/* If statement */

ifStatement
    : IF condition
      statement*
      (ELSE statement*)?
      END
    ;


/* Conditions */

condition
    : ID comparisonOperator NUMBER
    ;

comparisonOperator
    : GREATER
    | LESS
    | EQUAL
    ;


/* Loop */

loopStatement
    : LOOP NUMBER
      statement*
      END
    ;


/* Keywords */

DEVICE : 'DEVICE';
PIN    : 'PIN';

LED    : 'LED';
TEMP   : 'TEMP';
BUTTON : 'BUTTON';

ON     : 'ON';
OFF    : 'OFF';

WAIT   : 'WAIT';
READ   : 'READ';

IF     : 'IF';
ELSE   : 'ELSE';
END    : 'END';

LOOP   : 'LOOP';


/* Operators */

GREATER : '>';
LESS    : '<';
EQUAL   : '==';


/* General tokens */

NUMBER
    : [0-9]+
    ;

ID
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

WS
    : [ \t\r\n]+ -> skip
    ;