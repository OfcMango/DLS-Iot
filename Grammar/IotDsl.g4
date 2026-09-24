grammar IoTDSL;

program
    : statement* EOF
    ;

statement
    : deviceDeclaration
    | ledCommand
    | waitCommand
    ;

deviceDeclaration
    : DEVICE ID PIN NUMBER
    ;

ledCommand
    : LED (ON | OFF)
    ;

waitCommand
    : WAIT NUMBER
    ;

DEVICE : 'DEVICE';
PIN    : 'PIN';
LED    : 'LED';
ON     : 'ON';
OFF    : 'OFF';
WAIT   : 'WAIT';

ID
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

NUMBER
    : [0-9]+
    ;

WS
    : [ \t\r\n]+ -> skip
    ;