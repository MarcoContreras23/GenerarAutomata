from Resources.simbol import Simbol


class Alphabet:

    def __init__(self, simbols):
        self.simbols = []

    # Append a new simbol if that is valid
    def introSimbol(self, value, meaning):
        newSimbol = Simbol(value, meaning)
        validate = self.validateSimbol(newSimbol)
        if validate is True:
            self.simbols.append(newSimbol)

    # Function to validate if one simbol have value and meaning
    def validateSimbol(self, simbol):
        if simbol.value is not None and simbol.meaning is not None:
            return True
        else:
            return False
