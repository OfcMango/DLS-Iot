# Generated from IoTDSL.g4 by ANTLR 4.13.2
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
        4,1,19,91,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,37,8,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,5,
        7,59,8,7,10,7,12,7,62,9,7,1,7,1,7,5,7,66,8,7,10,7,12,7,69,9,7,3,
        7,71,8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,10,5,10,84,
        8,10,10,10,12,10,87,9,10,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,
        16,18,20,0,3,1,0,3,5,1,0,6,7,1,0,14,16,89,0,25,1,0,0,0,2,36,1,0,
        0,0,4,38,1,0,0,0,6,44,1,0,0,0,8,46,1,0,0,0,10,49,1,0,0,0,12,52,1,
        0,0,0,14,55,1,0,0,0,16,74,1,0,0,0,18,78,1,0,0,0,20,80,1,0,0,0,22,
        24,3,2,1,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,
        0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,37,3,
        4,2,0,31,37,3,8,4,0,32,37,3,10,5,0,33,37,3,12,6,0,34,37,3,14,7,0,
        35,37,3,20,10,0,36,30,1,0,0,0,36,31,1,0,0,0,36,32,1,0,0,0,36,33,
        1,0,0,0,36,34,1,0,0,0,36,35,1,0,0,0,37,3,1,0,0,0,38,39,5,1,0,0,39,
        40,5,18,0,0,40,41,3,6,3,0,41,42,5,2,0,0,42,43,5,17,0,0,43,5,1,0,
        0,0,44,45,7,0,0,0,45,7,1,0,0,0,46,47,5,18,0,0,47,48,7,1,0,0,48,9,
        1,0,0,0,49,50,5,8,0,0,50,51,5,17,0,0,51,11,1,0,0,0,52,53,5,9,0,0,
        53,54,5,18,0,0,54,13,1,0,0,0,55,56,5,10,0,0,56,60,3,16,8,0,57,59,
        3,2,1,0,58,57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,
        61,70,1,0,0,0,62,60,1,0,0,0,63,67,5,11,0,0,64,66,3,2,1,0,65,64,1,
        0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,71,1,0,0,0,69,
        67,1,0,0,0,70,63,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,73,5,12,
        0,0,73,15,1,0,0,0,74,75,5,18,0,0,75,76,3,18,9,0,76,77,5,17,0,0,77,
        17,1,0,0,0,78,79,7,2,0,0,79,19,1,0,0,0,80,81,5,13,0,0,81,85,5,17,
        0,0,82,84,3,2,1,0,83,82,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,
        1,0,0,0,86,88,1,0,0,0,87,85,1,0,0,0,88,89,5,12,0,0,89,21,1,0,0,0,
        6,25,36,60,67,70,85
    ]

class IoTDSLParser ( Parser ):

    grammarFileName = "IoTDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'DEVICE'", "'PIN'", "'LED'", "'TEMP'", 
                     "'BUTTON'", "'ON'", "'OFF'", "'WAIT'", "'READ'", "'IF'", 
                     "'ELSE'", "'END'", "'LOOP'", "'>'", "'<'", "'=='" ]

    symbolicNames = [ "<INVALID>", "DEVICE", "PIN", "LED", "TEMP", "BUTTON", 
                      "ON", "OFF", "WAIT", "READ", "IF", "ELSE", "END", 
                      "LOOP", "GREATER", "LESS", "EQUAL", "NUMBER", "ID", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_deviceDeclaration = 2
    RULE_deviceType = 3
    RULE_deviceCommand = 4
    RULE_waitCommand = 5
    RULE_readCommand = 6
    RULE_ifStatement = 7
    RULE_condition = 8
    RULE_comparisonOperator = 9
    RULE_loopStatement = 10

    ruleNames =  [ "program", "statement", "deviceDeclaration", "deviceType", 
                   "deviceCommand", "waitCommand", "readCommand", "ifStatement", 
                   "condition", "comparisonOperator", "loopStatement" ]

    EOF = Token.EOF
    DEVICE=1
    PIN=2
    LED=3
    TEMP=4
    BUTTON=5
    ON=6
    OFF=7
    WAIT=8
    READ=9
    IF=10
    ELSE=11
    END=12
    LOOP=13
    GREATER=14
    LESS=15
    EQUAL=16
    NUMBER=17
    ID=18
    WS=19

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
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 272130) != 0):
                self.state = 22
                self.statement()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
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


        def deviceCommand(self):
            return self.getTypedRuleContext(IoTDSLParser.DeviceCommandContext,0)


        def waitCommand(self):
            return self.getTypedRuleContext(IoTDSLParser.WaitCommandContext,0)


        def readCommand(self):
            return self.getTypedRuleContext(IoTDSLParser.ReadCommandContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(IoTDSLParser.IfStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(IoTDSLParser.LoopStatementContext,0)


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
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.deviceDeclaration()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.deviceCommand()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.waitCommand()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.readCommand()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.ifStatement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 35
                self.loopStatement()
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

        def deviceType(self):
            return self.getTypedRuleContext(IoTDSLParser.DeviceTypeContext,0)


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
            self.state = 38
            self.match(IoTDSLParser.DEVICE)
            self.state = 39
            self.match(IoTDSLParser.ID)
            self.state = 40
            self.deviceType()
            self.state = 41
            self.match(IoTDSLParser.PIN)
            self.state = 42
            self.match(IoTDSLParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeviceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LED(self):
            return self.getToken(IoTDSLParser.LED, 0)

        def TEMP(self):
            return self.getToken(IoTDSLParser.TEMP, 0)

        def BUTTON(self):
            return self.getToken(IoTDSLParser.BUTTON, 0)

        def getRuleIndex(self):
            return IoTDSLParser.RULE_deviceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeviceType" ):
                listener.enterDeviceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeviceType" ):
                listener.exitDeviceType(self)




    def deviceType(self):

        localctx = IoTDSLParser.DeviceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_deviceType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
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


    class DeviceCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IoTDSLParser.ID, 0)

        def ON(self):
            return self.getToken(IoTDSLParser.ON, 0)

        def OFF(self):
            return self.getToken(IoTDSLParser.OFF, 0)

        def getRuleIndex(self):
            return IoTDSLParser.RULE_deviceCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeviceCommand" ):
                listener.enterDeviceCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeviceCommand" ):
                listener.exitDeviceCommand(self)




    def deviceCommand(self):

        localctx = IoTDSLParser.DeviceCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_deviceCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(IoTDSLParser.ID)
            self.state = 47
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
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
        self.enterRule(localctx, 10, self.RULE_waitCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(IoTDSLParser.WAIT)
            self.state = 50
            self.match(IoTDSLParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(IoTDSLParser.READ, 0)

        def ID(self):
            return self.getToken(IoTDSLParser.ID, 0)

        def getRuleIndex(self):
            return IoTDSLParser.RULE_readCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadCommand" ):
                listener.enterReadCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadCommand" ):
                listener.exitReadCommand(self)




    def readCommand(self):

        localctx = IoTDSLParser.ReadCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_readCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(IoTDSLParser.READ)
            self.state = 53
            self.match(IoTDSLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(IoTDSLParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(IoTDSLParser.ConditionContext,0)


        def END(self):
            return self.getToken(IoTDSLParser.END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IoTDSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(IoTDSLParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(IoTDSLParser.ELSE, 0)

        def getRuleIndex(self):
            return IoTDSLParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = IoTDSLParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(IoTDSLParser.IF)
            self.state = 56
            self.condition()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 272130) != 0):
                self.state = 57
                self.statement()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 63
                self.match(IoTDSLParser.ELSE)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 272130) != 0):
                    self.state = 64
                    self.statement()
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 72
            self.match(IoTDSLParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IoTDSLParser.ID, 0)

        def comparisonOperator(self):
            return self.getTypedRuleContext(IoTDSLParser.ComparisonOperatorContext,0)


        def NUMBER(self):
            return self.getToken(IoTDSLParser.NUMBER, 0)

        def getRuleIndex(self):
            return IoTDSLParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = IoTDSLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(IoTDSLParser.ID)
            self.state = 75
            self.comparisonOperator()
            self.state = 76
            self.match(IoTDSLParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GREATER(self):
            return self.getToken(IoTDSLParser.GREATER, 0)

        def LESS(self):
            return self.getToken(IoTDSLParser.LESS, 0)

        def EQUAL(self):
            return self.getToken(IoTDSLParser.EQUAL, 0)

        def getRuleIndex(self):
            return IoTDSLParser.RULE_comparisonOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperator" ):
                listener.enterComparisonOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperator" ):
                listener.exitComparisonOperator(self)




    def comparisonOperator(self):

        localctx = IoTDSLParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
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


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOOP(self):
            return self.getToken(IoTDSLParser.LOOP, 0)

        def NUMBER(self):
            return self.getToken(IoTDSLParser.NUMBER, 0)

        def END(self):
            return self.getToken(IoTDSLParser.END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IoTDSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(IoTDSLParser.StatementContext,i)


        def getRuleIndex(self):
            return IoTDSLParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)




    def loopStatement(self):

        localctx = IoTDSLParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_loopStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(IoTDSLParser.LOOP)
            self.state = 81
            self.match(IoTDSLParser.NUMBER)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 272130) != 0):
                self.state = 82
                self.statement()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(IoTDSLParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





