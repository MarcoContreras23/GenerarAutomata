from Resources.er import ER
from Resources.alphabet import Alphabet


def main():
    alphabet = Alphabet([])
    alphabet.introSymbol('a', 'abrir')
    alphabet.introSymbol('ch', 'cerrar')
    #alphabet.introSymbol('ch', 'cerrar')
    symbols = []
    for symbol in alphabet.symbols:
        symbols.append(symbol.value)
    er = ER('a.ch', symbols)
    print(er.erValidate())
    print(er.buscar())

main()
