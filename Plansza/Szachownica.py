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
        self._iloscBicBialych = 0
        self._iloscBicCzarnych = 0
        self._iloscRuchowBialych = 0
        self._iloscRuchowCzarnych = 0

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

    def naPionku(self, *mouse, screen, turn):
        for raw in self._field:
            for pole in raw:
                x, y = pole.getPos()
                if pole.getNaPolu() == turn and x < mouse[0] < x + FLD and y < mouse [1] < y + FLD:
                    Funkcje.draw(x, y, screen, 'podswietlenie.png')
                    return pole
        return

    def setRuchy(self, i, j):
        self._field[i][j].setRuchy(self)

    def getRuchy(self, i, j):
        return self._field[i][j].getRuchy()

    def getIloscBicNaPlanszy(self):
        self._iloscBicBialych, self._iloscBicCzarnych  = 0, 0

        for row in self._field:
            for field in row:
                if field.getNaPolu() == FLD_WHITE:
                    self._iloscBicBialych += field.getIloscBic()
                elif field.getNaPolu() == FLD_BLACK:
                    self._iloscBicCzarnych += field.getIloscBic()
        return self._iloscBicBialych, self._iloscBicCzarnych

    def getIloscRuchowNaPlanszy(self):
        self._iloscBicBialych, self._iloscBicCzarnych = 0, 0
        for row in self._field:
            for field in row:
                if field.getNaPolu() == FLD_WHITE:
                    self._iloscRuchowBialych += field.getIloscRuchow()
                elif field.getNaPolu() == FLD_BLACK:
                    self._iloscBicCzarnych += field.getIloscRuchow()
        return self._iloscBicBialych, self._iloscBicCzarnych



