from antlr4 import *
from Frontend.generated.IoTDSLLexer import IoTDSLLexer
from Frontend.generated.IoTDSLParser import IoTDSLParser
from Frontend.error_listener import IoTErrorListener


input_stream = FileStream("Examples/test.iot")

lexer = IoTDSLLexer(input_stream)
token_stream = CommonTokenStream(lexer)

parser = IoTDSLParser(token_stream)

# Remove default ANTLR error messages
error_listener = IoTErrorListener()

lexer.removeErrorListeners()
parser.removeErrorListeners()

lexer.addErrorListener(error_listener)
parser.addErrorListener(error_listener)

# Parse
tree = parser.program()


# Result
if len(error_listener.errors) == 0:
    print("Parsing completed successfully!")
    print("No syntax errors found.")

    print("\nParse Tree:")
    print(tree.toStringTree(recog=parser))

else:
    print("Parsing failed.")
    print("\nSyntax Errors:")

    for error in error_listener.errors:
        print(error)