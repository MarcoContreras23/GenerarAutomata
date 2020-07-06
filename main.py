from Resources.er import ER
from Resources.alphabet import Alphabet


def main():
    alphabet = Alphabet([])
    alphabet.introSymbol('a', 'abrir')
    alphabet.introSymbol('b', 'cerrar')
    symbols = []
    for symbol in alphabet.symbols:
        symbols.append(symbol.value)
    er = ER('((a.b)+.a|a*.b.b?)', symbols)
    #print(er.erValidate())
    print(er.ERaPosfijo())
    

main()
