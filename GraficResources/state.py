"""
Autores: Camilo Gomez, Marco Contreras
version: 2.0
"""
#Clase con toda la estructura de que tiene un simbolo a la hora de graficar
class State:
  
    def __init__(self, inicio,final, transicion,adj):
        self.inicio = inicio
        self.final = final
        self.transicion = transicion
        self.adj = adj

