grammar IoTDSL;

program
    : statement* EOF
    ;

statement
    : deviceDeclaration
    | ledCommand
    | waitCommand
    | readCommand
    | ifStatement
    | loopStatement
    ;

deviceDeclaration
    : DEVICE deviceType PIN NUMBER
    ;

deviceType
    : LED
    | TEMP
    | BUTTON
    ;

ledCommand
    : LED (ON | OFF)
    ;

waitCommand
    : WAIT NUMBER
    ;

readCommand
    : READ deviceType
    ;

ifStatement
    : IF condition
      statement*
      (ELSE statement*)?
      END
    ;

condition
    : deviceType comparisonOperator NUMBER
    ;

comparisonOperator
    : GREATER
    | LESS
    | EQUAL
    ;

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