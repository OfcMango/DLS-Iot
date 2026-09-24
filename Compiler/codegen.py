from Output.IoTDSLListener import IoTDSLListener


class CodeGenerator(IoTDSLListener):

    def __init__(self):
        self.led_pin = None
        self.code = []

    def exitDeviceDeclaration(self, ctx):
        self.led_pin = ctx.NUMBER().getText()

    def exitLedCommand(self, ctx):
        if self.led_pin is None:
            return

        if ctx.ON():
            self.code.append(f"digitalWrite({self.led_pin}, HIGH);")

        elif ctx.OFF():
            self.code.append(f"digitalWrite({self.led_pin}, LOW);")

    def exitWaitCommand(self, ctx):
        number = ctx.NUMBER().getText()
        self.code.append(f"delay({number});")

    def generate(self):
        setup = [
            "void setup() {",
            f"    pinMode({self.led_pin}, OUTPUT);",
            "}",
            "",
            "void loop() {"
        ]

        for line in self.code:
            setup.append(f"    {line}")

        setup.append("}")

        return "\n".join(setup)