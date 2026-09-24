# Generated from grammar/IoTDSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,9,35,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,1,1,0,4,5,32,0,
        13,1,0,0,0,2,21,1,0,0,0,4,23,1,0,0,0,6,28,1,0,0,0,8,31,1,0,0,0,10,
        12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,
        0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,0,0,1,17,1,1,0,0,0,18,22,3,
        4,2,0,19,22,3,6,3,0,20,22,3,8,4,0,21,18,1,0,0,0,21,19,1,0,0,0,21,
        20,1,0,0,0,22,3,1,0,0,0,23,24,5,1,0,0,24,25,5,7,0,0,25,26,5,2,0,
        0,26,27,5,8,0,0,27,5,1,0,0,0,28,29,5,3,0,0,29,30,7,0,0,0,30,7,1,
        0,0,0,31,32,5,6,0,0,32,33,5,8,0,0,33,9,1,0,0,0,2,13,21
    ]

class IoTDSLParser ( Parser ):

    grammarFileName = "IoTDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'DEVICE'", "'PIN'", "'LED'", "'ON'", 
                     "'OFF'", "'WAIT'" ]

    symbolicNames = [ "<INVALID>", "DEVICE", "PIN", "LED", "ON", "OFF", 
                      "WAIT", "ID", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_deviceDeclaration = 2
    RULE_ledCommand = 3
    RULE_waitCommand = 4

    ruleNames =  [ "program", "statement", "deviceDeclaration", "ledCommand", 
                   "waitCommand" ]

    EOF = Token.EOF
    DEVICE=1
    PIN=2
    LED=3
    ON=4
    OFF=5
    WAIT=6
    ID=7
    NUMBER=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(IoTDSLParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IoTDSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(IoTDSLParser.StatementContext,i)


        def getRuleIndex(self):
            return IoTDSLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = IoTDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 74) != 0):
                self.state = 10
                self.statement()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(IoTDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def deviceDeclaration(self):
            return self.getTypedRuleContext(IoTDSLParser.DeviceDeclarationContext,0)


        def ledCommand(self):
            return self.getTypedRuleContext(IoTDSLParser.LedCommandContext,0)


        def waitCommand(self):
            return self.getTypedRuleContext(IoTDSLParser.WaitCommandContext,0)


        def getRuleIndex(self):
            return IoTDSLParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = IoTDSLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.deviceDeclaration()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.ledCommand()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.waitCommand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeviceDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEVICE(self):
            return self.getToken(IoTDSLParser.DEVICE, 0)

        def ID(self):
            return self.getToken(IoTDSLParser.ID, 0)

        def PIN(self):
            return self.getToken(IoTDSLParser.PIN, 0)

        def NUMBER(self):
            return self.getToken(IoTDSLParser.NUMBER, 0)

        def getRuleIndex(self):
            return IoTDSLParser.RULE_deviceDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeviceDeclaration" ):
                listener.enterDeviceDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeviceDeclaration" ):
                listener.exitDeviceDeclaration(self)




    def deviceDeclaration(self):

        localctx = IoTDSLParser.DeviceDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_deviceDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(IoTDSLParser.DEVICE)
            self.state = 24
            self.match(IoTDSLParser.ID)
            self.state = 25
            self.match(IoTDSLParser.PIN)
            self.state = 26
            self.match(IoTDSLParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LedCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LED(self):
            return self.getToken(IoTDSLParser.LED, 0)

        def ON(self):
            return self.getToken(IoTDSLParser.ON, 0)

        def OFF(self):
            return self.getToken(IoTDSLParser.OFF, 0)

        def getRuleIndex(self):
            return IoTDSLParser.RULE_ledCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLedCommand" ):
                listener.enterLedCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLedCommand" ):
                listener.exitLedCommand(self)




    def ledCommand(self):

        localctx = IoTDSLParser.LedCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ledCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(IoTDSLParser.LED)
            self.state = 29
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaitCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WAIT(self):
            return self.getToken(IoTDSLParser.WAIT, 0)

        def NUMBER(self):
            return self.getToken(IoTDSLParser.NUMBER, 0)

        def getRuleIndex(self):
            return IoTDSLParser.RULE_waitCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWaitCommand" ):
                listener.enterWaitCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWaitCommand" ):
                listener.exitWaitCommand(self)




    def waitCommand(self):

        localctx = IoTDSLParser.WaitCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_waitCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(IoTDSLParser.WAIT)
            self.state = 32
            self.match(IoTDSLParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





