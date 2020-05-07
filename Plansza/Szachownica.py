import os
import pygame
from email import message

from Plansza.Pole import Pole
from Plansza.Constant import *


class Szachownica:
    def __init__(self):
        self._field = [[Pole(i,j, FLD_EMPTY) for i in range(8)] for j in range(8)]
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

    def getPole(self, i, j):
        return self._field[i][j].getNaPolu()

    def naPionku(self, mouse):
        for pole in self._field:
            x, y = pole.getPos()
            if mouse[0] > x and x + FLD > mouse[0] and mouse [1] > y and y + FLD > mouse[1]:
                return True, pole
            return False






