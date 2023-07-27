#Tulio Castro Silva

import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from math import sin, cos, radians, pi


#Iniciando a janela 
pygame.init()
height = 600
width = 600
win = pygame.display.set_mode((height,width))

Var_angulo = Slider(win, 150, 20, 300, 10, min=0, max= 360, step=0.1)    #Slider que altera o angulo entre os galhos
Var_geracoes = Slider(win, 150, 50, 300, 10,min= 2, max = 9,step = 1)    #Slider que altera a quantidade de galhos


def Draw(x0, y0, angulo, geracao):
    """Funcao que desenha os galhos
    float, float, float, int -> None"""
    if geracao:
        x1 = x0 + int(cos(radians(angulo)) * geracao * 10.0)   
        y1 = y0 + int(sin(radians(angulo)) * geracao * 10.0)
        pygame.draw.line(win, (0,0,0), (x0, y0), (x1, y1), 2)
        Draw(x1, y1, angulo - Var_angulo.getValue()/4, geracao - 1)        #Desenhando o proximo galho para a esquerda
        Draw(x1, y1, angulo + Var_angulo.getValue()/4, geracao - 1)        #Desenhando o proximo galho para a direita



running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    win.fill((255, 255, 255))
    x = height/2
    Draw(300,550,-90,Var_geracoes.getValue())

    pygame_widgets.update(events)
    pygame.display.update()