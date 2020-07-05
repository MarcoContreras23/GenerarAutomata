from Resources.symbol import Symbol


class Alphabet:

    def __init__(self, symbols):
        self.symbols = []

    # Append a new simbol if that is valid
    def introSymbol(self, value, meaning):
        newSymbol = Symbol(value, meaning)
        validate = self.validateSymbol(newSymbol)
        if validate is True:
            self.symbols.append(newSymbol)

    # Function to validate if one symbol have value and meaning
    def validateSymbol(self, symbol):
        if symbol.value is not None and symbol.meaning is not None:
            return True
        else:
            return False
