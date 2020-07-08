from Resources.symbol import Symbol

"""
Autores: Camilo Gomez, Marco Contreras
version: 1.0
"""

class Alphabet:

    def __init__(self, symbols):
        self.symbols = []

    # Añade un nuevo simbolo si es valido
    def introSymbol(self, value, meaning):
        newSymbol = Symbol(value, meaning)
        validate = self.validateSymbol(newSymbol)
        if validate is True:
            self.symbols.append(newSymbol)

    # Metodo para validar que el simbolo tenga valor y significado
    def validateSymbol(self, symbol):
        if symbol.value is not None and symbol.meaning is not None:
            return True
        else:
            return False
