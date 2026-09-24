# Generated from grammar/IoTDSL.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by IoTDSLParser#ledCommand.
    def enterLedCommand(self, ctx:IoTDSLParser.LedCommandContext):
        pass

    # Exit a parse tree produced by IoTDSLParser#ledCommand.
    def exitLedCommand(self, ctx:IoTDSLParser.LedCommandContext):
        pass


    # Enter a parse tree produced by IoTDSLParser#waitCommand.
    def enterWaitCommand(self, ctx:IoTDSLParser.WaitCommandContext):
        pass

    # Exit a parse tree produced by IoTDSLParser#waitCommand.
    def exitWaitCommand(self, ctx:IoTDSLParser.WaitCommandContext):
        pass



del IoTDSLParser