import os
import sys
import pygame

from Funkcje import drawPionki, ustawPionek
from Komunikat import komunikatOPrzegranej, turaGracza
from Plansza import Szachownica
from Plansza.Constant import FLD_ALL, ROZMIAR_CZCIONKI

from Podswietlenie import podswietlenie

pygame.init()

windowSize = (FLD_ALL, FLD_ALL + ROZMIAR_CZCIONKI)

screen = pygame.display.set_mode(windowSize)

clock = pygame.time.Clock()

while 1:

    szachownica = Szachownica.Szachownica()
    turn = 0

    osGlownaPlansza = os.path.join('images', 'szachownica.png')
    imageGlownaPlansza = pygame.image.load(osGlownaPlansza)

    podswietlonePole = None

    run = True

    while run:

        clock.tick(30)

        screen.blit(imageGlownaPlansza, (0, 0))

        mousePosition = pygame.mouse.get_pos()

        podswietlonePole = podswietlenie(screen, szachownica, turn, mousePosition[0], mousePosition[1])

        drawPionki(szachownica, screen, turn)

        iloscRuchow = szachownica.getIloscRuchowNaPlanszy()
        iloscBic = szachownica.getIloscBicNaPlanszy()

        if iloscRuchow[turn] + iloscBic[turn] < 1:
            if komunikatOPrzegranej(turn, screen, mousePosition[0], mousePosition[1]) == True:
                run = False
        else:
            turaGracza(turn, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP and podswietlonePole:
                turn = ustawPionek(podswietlonePole, szachownica, turn, mousePosition[0], mousePosition[1])
                podswietlonePole.posX, podswietlonePole.posY = podswietlonePole.tempPosX, podswietlonePole.tempPosY #ustawianie na swoje miejsce zmienionego pola

        pygame.display.update()

