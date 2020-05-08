import os

import pygame

from Plansza.Constant import *


class Pole:
    def __init__(self, x, y, naPolu):
        self._indexX = x
        self._indexY = y
        self._posX = self._indexX*FLD
        self._posY = self._indexY*FLD
        self._naPolu = naPolu
        self._ruchy = dict()
        self._iloscRuchow = 0

    def getIndex(self):
        return self._indexX, self._indexY

    def getPos(self):
        return self._posX, self._posY

    def getNaPolu(self):
        return self._naPolu

    def setNaPolu(self, naPolu):
        self._naPolu = naPolu

    def setRuchy(self):
        pass


    def getRuchy(self):
        pass
