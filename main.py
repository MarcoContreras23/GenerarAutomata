from Resources.er import ER
from Resources.alphabet import Alphabet


def main():
    alphabet = Alphabet([])
    alphabet.introSymbol('a', 'abrir')
    alphabet.introSymbol('b', 'cerrar')
    er = ER('a|b', alphabet.symbols)
    #print(er.erValidate())
    print(er.erValidate())



    

main()
