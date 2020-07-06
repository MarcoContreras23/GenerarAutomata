from Resources.alphabet import Alphabet

# comprobacion de git


class ER:

    def __init__(self, er, symbols):
        self.er = er
        self.symbols = symbols
        self.characters = ['|', '.', '*', '+', '(', ')', '?', '[', ']', 'Ɛ']

    def inicio(self):
        self.recursiveComprobation(self.er[0], "")

    def recursiveComprobation(self, init, fin):
        newList = []
        if fin == self.er[len(self.er)-1]:
            return newList
        for i in range(len(self.er)-1):
            if init in self.symbols:
                newList.append(init)
                self.recursiveComprobation(
                    self.er[i+1], self.er[i+1])
            elif self.er[i] in self.characters:
                self.recursiveComprobation(
                    self.er[i+1], self.er[i+1])
            else:
                self.recursiveComprobation(
                    init + self.er[i+1], self.er[i+1])

    # Function to validate if all elements of ER are valids
    def erValidate(self):
        validation = True
        validateTerm = True
        symbols = []
        string = []
        for symbol in self.symbols:
            symbols.append(symbol)
        for element in self.er:
            print(element)
            for sym in symbols:
                string.append(sym)
            for char in self.characters:
                string.append(char)
            if element not in string:
                validation = False
        return validation

    def ERaPosfijo(self):
        posfijo =[]
        Nollaves = []

        for caracter in self.er:
            if caracter != '(':
                if caracter != ')':
                    Nollaves.append(caracter)
        for i in range(len(Nollaves)-1):
            if Nollaves[i] in self.characters:
                posfijo.append(Nollaves[i-1])
                posfijo.append(Nollaves[i+1])
                posfijo.append(Nollaves[i])
        print(posfijo)
        return True
                    

