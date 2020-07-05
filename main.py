from Resources.er import ER
from Resources.alphabet import Alphabet


def main():
    alphabet = Alphabet([])
    alphabet.introSymbol('a', 'abrir')
    #alphabet.introSimbol('b', 'cerrar')
    er = ER('a|', alphabet.symbols)
    #print(er.erValidate())
    print(er.erValidate())



    

main()
