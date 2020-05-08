import os
import sys

import pygame

from Funkcje import *
from Obiekt.Ruchy import ruchyOrazBicia
from Plansza import Szachownica
from Plansza.Constant import *

pygame.init()

windowSize = (FLD_ALL, FLD_ALL)

screen = pygame.display.set_mode(windowSize)

clock = pygame.time.Clock()
szachownica = Szachownica.Szachownica()
turn = 1

osGlownaPlansza = os.path.join('images', 'szachownica.png')
imageGlownaPlansza = pygame.image.load(osGlownaPlansza)

while 1:
    clock.tick(30)
    screen.blit(imageGlownaPlansza, (0, 0))

    mousePosition = pygame.mouse.get_pos()

    for i in range(8):
        for j in range(8):
            pole = szachownica.getPole(i, j)
            if pole != FLD_EMPTY:
                if pole == FLD_WHITE:
                    name = 'pionekBialy.png'
                elif pole == FLD_BLACK:
                    name = 'pionekCzarny.png'
                draw(i * FLD, j * FLD, screen, name)
                # to do wpisanie slownika do pola
                szachownica.setRuchy(i, j)

    if mousePosition[0] != -1 and not pygame.mouse.get_pressed()[0]:
        podswietlonePole = szachownica.naPionku(mousePosition[0], mousePosition[1], screen=screen)  # podswitlenie pionka

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            pass

    pygame.display.update()