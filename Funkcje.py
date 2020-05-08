import os

import pygame

from Plansza.Constant import *


def podniesPionek(pole, *mouse):
    pass


def draw(x, y, screen, name):
    osImage = os.path.join('images', name)
    image = pygame.image.load(osImage)
    if image.get_alpha is None:
        image = image.convert()
    else:
        image = image.convert_alpha()
    image = pygame.transform.scale(image, (FLD, FLD))
    screen.blit(image, (x, y))