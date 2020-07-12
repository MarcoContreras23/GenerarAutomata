from Resources.alphabet import Alphabet
from GraficResources.automaton import *

"""
Autores: Camilo Gomez, Marco Contreras
version: 6.0
"""

#Clase para evaluar la expresion regular
class ER:

    def __init__(self, er, symbols):
        self.er = er
        self.symbols = symbols
        self.characters = ['|', '.', '*', '+', '(', ')', '?', '[', ']', 'Ɛ']
        self.automaton = Automaton()
        self.validation = False
        self.cadena = ''
        self.N = 50
        self.pila = []
        self.EP = []
        self.tope = -1
        self.udt=list('+*?')

    # Metodo para validar que la ER concuerde con el alfabeto previamente asignado
    def erValidate(self, cursor, value):
        if value == False:
            return False
        for element in self.er:
            if cursor == len(self.er):
                self.validation = True
                return self.validation
            elif element == self.er[cursor] and cursor < len(self.er):
                if element not in self.characters:
                    self.cadena = self.cadena + element
                    self.erValidate(cursor+1, True)
                    break
                elif element in self.characters:
                    if self.cadena in self.symbols:
                        self.cadena = ''
                        self.validation = True
                        self.erValidate(cursor+1, True)
                        break
                    else:
                        self.validation = False
                        self.erValidate(cursor+1, False)
                        break
        return self.validation

    def llena(self):
        if(self.tope == (self.N-1)):
            return True
        return False

    def vacia(self):
        if(self.tope == -1):
            return True
        return False

    def push(self,dato):
        if(self.llena()!=True):
            global tope
            self.tope = self.tope+1
            self.pila.insert(self.tope,dato)

    def pop(self):
        if(self.vacia() != True):
            global tope
            aux = self.pila[self.tope]
            del self.pila[self.tope]
            self.tope = self.tope-1
            return aux
        else:
            return -9999
            
    def infijo(self,i, EI):
        if(EI[i]=='^'):
            prioridadop=4
            return prioridadop
        elif(EI[i]=='.'):
            prioridadop=2
            return prioridadop
        elif(EI[i]=='/'):
            prioridadop=2
            return prioridadop
        elif(EI[i]=='|'):
            prioridadop=1
            return prioridadop
        elif(EI[i]=='-'):
            prioridadop=1
            return prioridadop
        elif(EI[i]=='('):
            prioridadop=5
            return prioridadop

    def pripila(self,pila):
        if(self.pila[self.tope]=='^'):
            prioridadpi=3
            return prioridadpi
        elif(self.pila[self.tope]=='.'):
            prioridadpi=2
            return prioridadpi
        elif(self.pila[self.tope]=='/'):
            prioridadpi=2
            return prioridadpi
        elif(self.pila[self.tope]=='|'):
            prioridadpi=1
            return prioridadpi
        elif(self.pila[self.tope]=='-'):
            prioridadpi=1
            return prioridadpi
        elif(self.pila[self.tope]=='('):
            prioridadpi= 0
            return prioridadpi
                    

    def ERaPF(self,er):
        EI=list(self.er)

        for i in range(len(EI)):
            if(EI[i] in self.symbols or EI[i] in self.udt):      
                self.EP.append(EI[i])
            elif(EI[i]!=')'):                      
                if (self.tope == -1):                    
                    self.push(EI[i])
                else:
                    if(self.infijo(i,EI) <= self.pripila(self.pila)):
                        self.EP.append(self.pop())
                        self.push(EI[i])
                    elif(self.infijo(i,EI) > self.pripila(self.pila)):
                        self.push(EI[i])
            elif(EI[i]==')'):                    
                while (self.pila[self.tope]!='('):         
                    self.EP.append(self.pop())
                if(self.pila[self.tope]=='('):              
                    self.pop()
                elif(self.tope!=-1):                    
                    self.EP.append(self.pop())
        while (self.tope > -1):
            self.EP.append(self.pop())

        H = []
        H = self.EP.copy()
        self.EP.clear()
        return (''.join(H))