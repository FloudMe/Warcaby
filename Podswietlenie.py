import pygame

from Funkcje import podniesPionek


def podswietlenie(screen, szachownica, turn, *mouse):
    global podswietlonePole

    if mouse[0] != -1 and not pygame.mouse.get_pressed()[0]:
        podswietlonePole = szachownica.naPionku(mouse[0], mouse[1], screen=screen, turn=turn)  # podswitlenie pionka

    if pygame.mouse.get_pressed()[0] and podswietlonePole:
        if podswietlonePole.iloscRuchow > 0 and szachownica.getIloscBicNaPlanszy()[turn] == 0 or podswietlonePole.iloscBic > 0:
            podniesPionek(podswietlonePole, screen, mouse[0], mouse[1]) #podniesienie pionka

    return podswietlonePole