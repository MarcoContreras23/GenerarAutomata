from GraficResources.state import State
from Resources.er import *

"""
Autores: Camilo Gomez, Marco Contreras
version: 2.0
"""
#Clase que contiene toda la administración del automata
class Automaton:

    def __init__(self):
        self.root = None
        self.states = []

    #Añadé cada estado a una lista de estados
    def añadirEstado(self,state):
        if state not in self.states:
            self.states.append(state)

    #Operaciones para realizar el automata por el minimo de transiciones lambda
    def MinLambda(self):
        pass


    def addRoot(self, value,meaning ,adj, pos):
        if self.root is None:
            self.root = State(value, meaning, adj, pos)
            self.states.append(self.root)
        elif self.root is None:
            self.addNode(self.root)

    def addNode(self, node):
        if node not in self.states:
            self.states.append(node)
