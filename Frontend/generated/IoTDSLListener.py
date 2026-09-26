# Generated from IoTDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IoTDSLParser import IoTDSLParser
else:
    from IoTDSLParser import IoTDSLParser

# This class defines a complete listener for a parse tree produced by IoTDSLParser.
class IoTDSLListener(ParseTreeListener):

    # Enter a parse tree produced by IoTDSLParser#program.
    def enterProgram(self, ctx:IoTDSLParser.ProgramContext):
        pass

    # Exit a parse tree produced by IoTDSLParser#program.
    def exitProgram(self, ctx:IoTDSLParser.ProgramContext):
        pass


    # Enter a parse tree produced by IoTDSLParser#statement.
    def enterStatement(self, ctx:IoTDSLParser.StatementContext):
        pass

    # Exit a parse tree produced by IoTDSLParser#statement.
    def exitStatement(self, ctx:IoTDSLParser.StatementContext):
        pass


    # Enter a parse tree produced by IoTDSLParser#deviceDeclaration.
    def enterDeviceDeclaration(self, ctx:IoTDSLParser.DeviceDeclarationContext):
        pass

    # Exit a parse tree produced by IoTDSLParser#deviceDeclaration.
    def exitDeviceDeclaration(self, ctx:IoTDSLParser.DeviceDeclarationContext):
        pass


    # Enter a parse tree produced by IoTDSLParser#deviceType.
    def enterDeviceType(self, ctx:IoTDSLParser.DeviceTypeContext):
        pass

    # Exit a parse tree produced by IoTDSLParser#deviceType.
    def exitDeviceType(self, ctx:IoTDSLParser.DeviceTypeContext):
        pass


    # Enter a parse tree produced by IoTDSLParser#deviceCommand.
    def enterDeviceCommand(self, ctx:IoTDSLParser.DeviceCommandContext):
        pass

    # Exit a parse tree produced by IoTDSLParser#deviceCommand.
    def exitDeviceCommand(self, ctx:IoTDSLParser.DeviceCommandContext):
        pass


    # Enter a parse tree produced by IoTDSLParser#waitCommand.
    def enterWaitCommand(self, ctx:IoTDSLParser.WaitCommandContext):
        pass

    # Exit a parse tree produced by IoTDSLParser#waitCommand.
    def exitWaitCommand(self, ctx:IoTDSLParser.WaitCommandContext):
        pass


    # Enter a parse tree produced by IoTDSLParser#readCommand.
    def enterReadCommand(self, ctx:IoTDSLParser.ReadCommandContext):
        pass

    # Exit a parse tree produced by IoTDSLParser#readCommand.
    def exitReadCommand(self, ctx:IoTDSLParser.ReadCommandContext):
        pass


    # Enter a parse tree produced by IoTDSLParser#ifStatement.
    def enterIfStatement(self, ctx:IoTDSLParser.IfStatementContext):
        pass

    # Exit a parse tree produced by IoTDSLParser#ifStatement.
    def exitIfStatement(self, ctx:IoTDSLParser.IfStatementContext):
        pass


    # Enter a parse tree produced by IoTDSLParser#condition.
    def enterCondition(self, ctx:IoTDSLParser.ConditionContext):
        pass

    # Exit a parse tree produced by IoTDSLParser#condition.
    def exitCondition(self, ctx:IoTDSLParser.ConditionContext):
        pass


    # Enter a parse tree produced by IoTDSLParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:IoTDSLParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by IoTDSLParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:IoTDSLParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by IoTDSLParser#loopStatement.
    def enterLoopStatement(self, ctx:IoTDSLParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by IoTDSLParser#loopStatement.
    def exitLoopStatement(self, ctx:IoTDSLParser.LoopStatementContext):
        pass



del IoTDSLParser