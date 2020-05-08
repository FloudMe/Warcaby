import os
import pygame
from email import message

import Funkcje
from Plansza.Pole import Pole
from Plansza.Constant import *


class Szachownica:
    def __init__(self):
        self._field = [[Pole(j,i, FLD_EMPTY) for i in range(8)] for j in range(8)]
        self.setList()

    def setList(self):
        for i in range(4):
            for j in range(3):
                x = 1 + i * 2 - j % 2
                y = j
                self._field[x][y].setNaPolu(FLD_BLACK)
        for i in range(4):
            for j in range(3):
                x = i * 2 + j % 2
                y = 7 - j
                self._field[x][y].setNaPolu(FLD_WHITE)

    def getCurrentField(self, i, j):
        return self._field[i][j]

    def getPole(self, i, j):
        return self._field[i][j].getNaPolu()

    def naPionku(self, *mouse, screen):
        for raw in self._field:
            for pole in raw:
                x, y = pole.getPos()
                if pole.getNaPolu() != FLD_EMPTY and x < mouse[0] < x + FLD and y < mouse [1] < y + FLD:
                    Funkcje.draw(x, y, screen, 'podswietlenie.png')
                    return pole
        return

    def setRuchy(self, i, j):
        pass

    def getRuchy(self):
        pass




