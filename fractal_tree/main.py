import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import math
from math import pi

pygame.init()
height = 600
width = 600
win = pygame.display.set_mode((height,width))

Var_angulo = Slider(win, 150, 20, 300, 10, min=0, max= 360, step=0.1)
Var_geracoes = Slider(win, 150, 50, 300, 10,min= 2, max = 9,step = 1)


def Draw(x0, y0, angulo, geracao):
    if geracao:
        x1 = x0 + int(math.cos(math.radians(angulo)) * geracao * 10.0)
        y1 = y0 + int(math.sin(math.radians(angulo)) * geracao * 10.0)
        pygame.draw.line(win, (0,0,0), (x0, y0), (x1, y1), 2)
        Draw(x1, y1, angulo - Var_angulo.getValue()/4, geracao - 1)
        Draw(x1, y1, angulo + Var_angulo.getValue()/4, geracao - 1)


run = True
while run:
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