from GraficResources.Transition import Transition
from Resources.er import *
from Resources.alphabet import *

"""
Autores: Camilo Gomez, Marco Contreras
version: 2.0
"""
# Clase que contiene toda la administración del automata


class Automaton:

    def _init_(self):
        self.root = None
        self.states = []
        self.pila = []
        self.cadena = []
        

    # Añadé cada estado a una lista de estados
    def añadirEstado(self, state):
        if state not in self.states:
            self.states.append(state)

    # Operaciones para realizar el automata por thompson
    def thompson(self,cadenaPost,cursor,symbols,characters):
        for element in cadenaPost:
            if element == "Ɛ":
                pass
            if element in symbols:
                pass


    def Stack(self, cadenaPost, cursor, symbols, characters):
        for element in cadenaPost:
            if cursor == len(cadenaPost):
                return pila
            elif element == cadenaPost[cursor] and cursor < len(cadenaPost):
                if cursor <= len(cadenaPost)-2:

                    # automata de un simbolo, solo se agrega una transicion
                    if element in symbols and (cadenaPost[cursor+1] != '*' or cadenaPost[cursor+1] != '+' or cadenaPost[cursor+1] != '?'):
                        newTransition = Transition([(cursor, cursor+1,
                                                     element)])
                        self.cadena.append(newTransition)
                        self.Stack(cadenaPost, cursor+1, symbols, characters)
                        break

                    # automata con . se agrega una transicion entre el estado final del primero y el estado inicial del segundo
                    if element is '.' and len(self.cadena) != 0:
                        newTransition = Transition(
                            (self.cadena[0].final, self.cadena[1].inicio, 'Ɛ'))
                        for value in self.cadena:
                            self.cadena.pop(value)
                        self.cadena.append(newTransition)
                        self.Stack(cadenaPost, cursor+1, symbols, characters)
                        break

                    # automata con + se agregan 3 transiciones, una del primer estado nuevo a la inicial del automata con Ɛ
                    # otra transicion del estado final del automata al inicial con Ɛ
                    # y una ultima del estado final del automata al segundo estado nuevo con Ɛ
                    if element is '+' and len(self.cadena) != 0:
                        newTransition = Transition([(q1, self.cadena[0].inicial, 'Ɛ'), (
                            self.cadena[0].final, self.cadena[0].inicial, 'Ɛ'), ((self.cadena[0].final, q2, 'Ɛ'))])
                        for value in self.cadena:
                            self.cadena.pop(value)
                        self.cadena.append(newTransition)
                        self.Stack(cadenaPost, cursor+1, symbols, characters)

                    # automata con * se agregan 4 transiciones, una del primer estado nuevo a la inicial del automata con Ɛ
                    # otra transicion del estado final del automata al inicial con Ɛ
                    # otra del estado final del automata al segundo estado nuevo con Ɛ
                    # y una ultima del primer nuevo estado al segundo nuevo estado con Ɛ
                    if element is '*' and len(self.cadena) != 0:
                        newTransition = Transition([(q1, self.cadena[0].inicial, 'Ɛ'), (self.cadena[0].final, self.cadena[0].inicial, 'Ɛ'),
                                                    (self.cadena[0].final, q2, 'Ɛ'), (q1, q2, 'Ɛ')])
                        for value in self.cadena:
                            self.cadena.pop(value)
                        self.cadena.append(newTransition)
                        self.Stack(cadenaPost, cursor+1, symbols, characters)

                    # automata con ? se agrega 1 transicion, una del primer estado nuevo segundo estado nuevo con Ɛ
                    if element is '?' and len(self.cadena) != 0:
                        newTransition = Transition([(q1, q2, 'Ɛ')])
                        for value in self.cadena:
                            self.cadena.pop(value)
                        self.cadena.append(newTransition)
                        self.Stack(cadenaPost, cursor+1, symbols, characters)

                    # automata con | se agregan 4 transiciones, una del primer estado nuevo al inicial del primer auntomata en la fila con Ɛ
                    # otra del primer estado nuevo al inicial del segundo automata con Ɛ
                    # otra del estado final del primer automata al segundo estado nuevo con Ɛ
                    # y una ultima del estado final del segundo automata al segundo estado nuevo con Ɛ
                    if element is '|' and len(self.cadena) != 0:
                        newTransition = Transition([(q1, self.cadena[0].inicial, 'Ɛ'), (q1, self.cadena[1].inicial, 'Ɛ'),
                                                    (self.cadena[0].final, q2, 'Ɛ'), (self.cadena[1].final, q2, 'Ɛ')])
                        for value in self.cadena:
                            self.cadena.pop(value)
                        self.cadena.append(newTransition)
                        self.Stack(cadenaPost, cursor+1, symbols, characters)