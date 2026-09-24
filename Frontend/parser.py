from antlr4 import FileStream, CommonTokenStream

from Frontend.generated.IoTDSLLexer import IoTDSLLexer
from Frontend.generated.IoTDSLParser import IoTDSLParser
from Frontend.error_listener import IoTErrorListener


def parse_file(file_path):

    input_stream = FileStream(file_path)

    lexer = IoTDSLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    parser = IoTDSLParser(token_stream)

    error_listener = IoTErrorListener()

    lexer.removeErrorListeners()
    parser.removeErrorListeners()

    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)

    tree = parser.program()

    return tree, error_listener.errors