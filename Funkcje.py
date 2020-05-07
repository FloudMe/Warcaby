import pygame

from Plansza.Constant import *


def podniesPionek():
    pass


def draw(x, y, pole, screen):
    if pole == FLD_WHITE:
        pionek = pygame.image.load("images\\pionekBialy.png")
    elif pole == FLD_BLACK:
        pionek = pygame.image.load("images\\pionekCzarny.png")
    if pionek.get_alpha is None:
        pionek = pionek.convert()
    else:
        pionek = pionek.convert_alpha()
    pionek = pygame.transform.scale(pionek, (FLD, FLD))
    screen.blit(pionek, (x, y))