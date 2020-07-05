from Resources.er import ER
from Resources.alphabet import Alphabet


def main():
    alphabet = Alphabet([])
    alphabet.introSimbol('a', 'abrir')
    #alphabet.introSimbol('b', 'cerrar')
    er = ER('a|', alphabet.simbols)
    #print(er.erValidate())
    print(er.validar())



    

main()
