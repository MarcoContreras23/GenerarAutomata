import pygame
"""
Autores: Camilo Gomez, Marco Contreras
version: 2.0
"""
#clase para capturar la posicion del cursor
class Cursor(pygame.Rect):

    def __init__(self):
        super(Cursor,Cursor). __init__(self,0,0,1,1)

    def update(self):
        self.left,self.top = pygame.mouse.get_pos()