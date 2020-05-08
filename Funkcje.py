import os

import pygame

from Plansza.Constant import *

def podniesPionek(pole, screen, szachownica, turn, *mouse):
    pole.setTempPos(mouse[0], mouse[1])
    for key, value in pole.getRuchy().items():
        if (szachownica.getIloscBicNaPlanszy()[turn] < 1) or (pole.getIloscBic() > 0 and value !=0):
            draw(key[0] * FLD, key[1] * FLD, screen, 'podswietlenie.png')

def ustawPionek(pole, szachownica, turn, *mouse):
    for key, value in pole.getRuchy().items():
        if key[0] * FLD < mouse[0] < (key[0] * FLD) + FLD and key[1] * FLD < mouse [1] < (key[1] * FLD) + FLD:
            if szachownica.getIloscBicNaPlanszy()[turn] > 0:
                if pole.getIloscBic() < 1:
                    return turn
                pole.setNaPolu(FLD_EMPTY)
                pole = szachownica.getCurrentField(key[0], key[1])
                pole.setNaPolu(turn)
                szachownica.getCurrentField(value[0], value[1]).setNaPolu(FLD_EMPTY)
                pole.setRuchy(szachownica)
                if pole.getIloscBic() > 0:
                    return turn
            elif value == 0 and szachownica.getIloscBicNaPlanszy()[turn] < 1:
                pole.setNaPolu(FLD_EMPTY)
                szachownica.getCurrentField(key[0], key[1]).setNaPolu(turn)
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