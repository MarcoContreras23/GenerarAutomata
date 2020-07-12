import sys
import os
from tkinter import *
from pygame.locals import *
from pygame import Rect
import threading
import ctypes
import pygame
from GUI.Button import *
from GUI.Cursor import *
from Resources.alphabet import Alphabet
from Resources.er import ER
"""
Autores: Camilo Gomez, Marco Contreras
version: 2.0
"""
pygame.init()
pygame.font.init()

#Clase encargada de mostrar la parte grafica
class GUI:

    def __init__(self,simbolo):
        self.simbolo = simbolo
        self.cursor = Cursor()
        self.alphabet = Alphabet([])
        self.er = ER([],self.alphabet)
        self.all()
        

    #Metodo para establerzer tamaño de la ventana en windows

    def screen_sizeW(self):
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        size = (ancho, alto)
        return size

    def all(self):

        display = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
        pygame.display.set_caption("Automata")
        fuente = pygame.font.SysFont('Comic Sans MS', 15)
        # Cargar las images
        button = pygame.image.load("C:\\Users\\marco\\OneDrive\\Documentos\\Automatas\\Proyecto1\\GUI\\Images\\button.png")
        # Escalar imagenes
        button = pygame.transform.scale(button, (140, 75))
        # Asignacion de botones
        boton = ButtonP(button, button, 350, 20)
        # Texto para el boton
        prueba = fuente.render("Prueba", True, (0, 0, 0))

        #Prueba ventana
        while True:

                display.fill((100, 195, 199))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.cursor.colliderect(boton.rect):
                            screenTK3 = Tk()
                            size = self.screen_sizeW()
                            screenTK3.geometry(
                                f"430x150+{int(size[0] / 2) - 230}+{int(size[1] / 2) - 100}")
                            screenTK3.title(
                                "Backpacker")
                            textC = StringVar(
                                    value="Ingrese el alfabeto")
                            labelC = Label(
                                screenTK3, textvariable=textC).place(x=150, y=10)
                            texcT =StringVar(
                                value="Ingrese la expresión regular")
                            labelT= Label(
                                screenTK3,textvariable=texcT).place(x=150,y=50)
                            Cost_field = Entry(
                                screenTK3, textvariable=self.alphabet.introSymbol, width=25).place(x=150, y=30)
                            time_field = Entry(
                                 screenTK3, textvariable = self.er.symbols, width=25).place(x=150 , y=70)
                            Button(screenTK3, text="OK",
                                 command=lambda: self.er.erValidate()).place(x=150, y=100)
                            
                            screenTK3.mainloop()
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                self.cursor.update()
                boton.update(display, self.cursor,prueba)
                pygame.display.update()