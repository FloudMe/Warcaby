import os
import sys

import pygame

from Funkcje import *
from Plansza import Szachownica
from Plansza.Constant import *


pygame.init()

windowSize = (FLD_ALL, FLD_ALL)

screen = pygame.display.set_mode(windowSize)

clock = pygame.time.Clock()
szachownica = Szachownica.Szachownica()

imageGlownaPlansza = pygame.image.load("images\\szachownica.png")

while 1:
    clock.tick(30)
    screen.blit(imageGlownaPlansza, (0,0))
    p = 0
    for i in range(8):
        for j in range(8):
            pole = szachownica.getPole(i, j)
            if pole != FLD_EMPTY:
                draw( i * FLD, j * FLD, pole, screen )
    mousePosition = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.mouse.get_pressed():
            zapytanie, pole = szachownica.naPionku(mousePosition)
            if zapytanie == True:
                szachownica.podniesPionek(pole)
    pygame.display.update()