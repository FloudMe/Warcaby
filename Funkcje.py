import os

import pygame

from Plansza.Constant import FLD, FLD_EMPTY, FLD_WHITE, FLD_BLACK, FLD_WHITE_DAMKA, FLD_BLACK_DAMKA

def podniesPionek(pole, screen, *mouse):
    pole.posX, pole.posY = mouse[0] - (FLD / 2), mouse[1] - (FLD / 2)
    for key, value in pole.ruchy.items():
        if (pole.iloscBic > 0 and value !=0):
            draw(key[0] * FLD, key[1] * FLD, screen, 'podswietlenie.png')
        elif pole.iloscBic < 1:
            draw(key[0] * FLD, key[1] * FLD, screen, 'podswietlenie.png')

def ustawPionek(pole, szachownica, turn, *mouse):
    for key, value in pole.ruchy.items():
        if key[0] * FLD < mouse[0] < (key[0] * FLD) + FLD and key[1] * FLD < mouse [1] < (key[1] * FLD) + FLD:
            if szachownica.getIloscBicNaPlanszy()[turn] > 0:
                if pole.iloscBic < 1 or value == 0:
                    return turn

                szachownica.field[key[0]][key[1]].naPolu = pole.naPolu
                pole.naPolu = FLD_EMPTY
                pole = szachownica.field[key[0]][key[1]]

                szachownica.field[value[0]][value[1]].naPolu = FLD_EMPTY
                pole.setRuchy(szachownica)

                if ( (key[1] == 0 and pole.naPolu == FLD_WHITE) or (key[1] == 7 and pole.naPolu == FLD_BLACK) ) and pole.iloscBic < 1 and pole.naPolu not in [FLD_WHITE_DAMKA, FLD_BLACK_DAMKA]:
                    pole.naPolu += 2

                elif pole.iloscBic > 0:
                    return turn

            elif value == 0 and szachownica.getIloscBicNaPlanszy()[turn] < 1:
                szachownica.field[key[0]][key[1]].naPolu = pole.naPolu
                pole.naPolu = FLD_EMPTY
                if (key[1] == 0 and szachownica.field[key[0]][key[1]].naPolu == FLD_WHITE) or (key[1] == 7 and szachownica.field[key[0]][key[1]].naPolu == FLD_BLACK):
                    szachownica.field[key[0]][key[1]].naPolu += 2

            turn += 1
            return turn % 2
    return turn

def draw(x, y, screen, name):
    osImage = os.path.join('images', name)
    image = pygame.image.load(osImage)
    if image.get_alpha is None:
        image = image.convert()
    else:
        image = image.convert_alpha()
    image = pygame.transform.scale(image, (FLD, FLD))
    screen.blit(image, (x, y))

def drawPionki(szachownica, screen, turn):
    pionki = szachownica.getListaPol()
    global pom
    if turn == FLD_WHITE:
        pom = [FLD_BLACK, FLD_BLACK_DAMKA, FLD_WHITE, FLD_WHITE_DAMKA]
    else:
        pom = [FLD_WHITE, FLD_WHITE_DAMKA, FLD_BLACK, FLD_BLACK_DAMKA]
    for i in pom:
        for p in pionki[i]:
            draw(p.posX, p.posY, screen, str(i) + '.png')
            p.setRuchy(szachownica)