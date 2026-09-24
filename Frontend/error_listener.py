from antlr4.error.ErrorListener import ErrorListener


class IoTErrorListener(ErrorListener):

    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(
        self,
        recognizer,
        offendingSymbol,
        line,
        column,
        msg,
        e
    ):
        error = f"Syntax Error at line {line}, column {column}: {msg}"
        self.errors.append(error)

    def reportAmbiguity(
        self,
        recognizer,
        dfa,
        startIndex,
        stopIndex,
        exact,
        ambigAlts,
        configs
    ):
        pass

    def reportAttemptingFullContext(
        self,
        recognizer,
        dfa,
        startIndex,
        stopIndex,
        conflictingAlts,
        configs
    ):
        pass

    def reportContextSensitivity(
        self,
        recognizer,
        dfa,
        startIndex,
        stopIndex,
        prediction,
        configs
    ):
        pass