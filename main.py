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
turn = 0

osGlownaPlansza = os.path.join('images', 'szachownica.png')
imageGlownaPlansza = pygame.image.load(osGlownaPlansza)

podswietlonePole = None

while 1:

    clock.tick(30)

    screen.blit(imageGlownaPlansza, (0, 0))

    mousePosition = pygame.mouse.get_pos()

    for i in range(8):
        for j in range(8):
            naPolu = szachownica.getPole(i, j)
            if naPolu != FLD_EMPTY:
                if naPolu == FLD_WHITE:
                    name = 'pionekBialy.png'
                elif naPolu == FLD_BLACK:
                    name = 'pionekCzarny.png'
                x, y = szachownica.getCurrentField(i, j).getPos()
                draw(x, y, screen, name)
                szachownica.setRuchy(i, j)

    if mousePosition[0] != -1 and not pygame.mouse.get_pressed()[0]:
        podswietlonePole = szachownica.naPionku(mousePosition[0], mousePosition[1], screen=screen, turn=turn)  # podswitlenie pionka

    if pygame.mouse.get_pressed()[0] and podswietlonePole:
        if podswietlonePole.getIloscRuchow() > 0 and szachownica.getIloscBicNaPlanszy()[turn] == 0 or podswietlonePole.getIloscBic() > 0:
            podniesPionek(podswietlonePole, screen, szachownica, turn, mousePosition[0], mousePosition[1]) #podniesienie pionka

    iloscRuchow = szachownica.getIloscRuchowNaPlanszy()

    if iloscRuchow[turn] > 0:
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP and podswietlonePole:
            turn = ustawPionek(podswietlonePole, szachownica, turn, mousePosition[0], mousePosition[1])
            podswietlonePole.setTemp() #ustawianie na swoje miejsce zmienionego pola

    pygame.display.update()

