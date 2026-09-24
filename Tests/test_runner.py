import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from antlr4 import FileStream, CommonTokenStream
from Frontend.generated.IoTDSLLexer import IoTDSLLexer
from Frontend.generated.IoTDSLParser import IoTDSLParser


test_files = [
    ("basic_led.iot", True),
    ("sensor.iot", True),
    ("condition.iot", True),
    ("loop.iot", True),
    ("multiple_devices.iot", True),
    ("invalid.iot", False)
]


for filename, should_pass in test_files:

    print("=" * 50)
    print("Testing:", filename)

    path = os.path.join("Examples", filename)

    input_stream = FileStream(path)

    lexer = IoTDSLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    parser = IoTDSLParser(token_stream)

    parser.program()

    errors = parser.getNumberOfSyntaxErrors()

    if should_pass and errors == 0:
        print("RESULT: PASS")

    elif not should_pass and errors > 0:
        print("RESULT: PASS (Invalid syntax detected)")

    else:
        print("RESULT: FAIL")