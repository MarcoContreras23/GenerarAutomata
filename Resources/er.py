from Resources.alphabet import Alphabet


class ER:

    def __init__(self, er, simbols):
        self.er = er
        self.simbols = simbols
        self.characters = ['|', '.', '+', '⁺', '(', ')', '?']

    # Function to validate if all elements of ER are valids
    def erValidate(self):
        validation = False
        simbols = []
        for simbol in self.simbols:
            simbols.append(simbol)
        for element in self.er:
            if element not in simbols and element not in self.characters:
                print(element)
                validation = True
                return validation
        return validation

    def validar(self):
        validacion = False
        simbolos = []
        ER = []
        
        for simbolo in self.simbols:
            simbolos.append(simbolo)
            print(simbolo.value)
        for elemento in self.er:
            print(elemento) 
            
            if elemento in simbolos:
                ER.append(elemento)
        for caracter in self.characters:
            if caracter in ER:
                validacion = True
                return True
        return validacion
