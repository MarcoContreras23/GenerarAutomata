from Resources.er import ER
from Resources.alphabet import Alphabet
from GUI.GUI import *

"""
Autores: Camilo Gomez, Marco Contreras
version: 3.0
"""
class main:

    alphabet = Alphabet([])
    if __name__ == '__main__':
        alphabet.introSymbol('a', 'abrir')
        gui = GUI(alphabet)

    #Main anterior por si desea verlo
    """
    alphabet.introSymbol('b', 'cerrar')
    symbols = []
    for symbol in alphabet.symbols:
        symbols.append(symbol.value)
    er = ER('((a.b)+.a|a*.b.b?)', symbols)
    #print(er.erValidate())
    print(er.ERaPosfijo())"""