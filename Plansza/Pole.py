import os

import pygame

from Plansza.Constant import *


class Pole:
    def __init__(self, x, y, naPolu):
        self._indexX = x
        self._indexY = y
        self._posX = self._indexX*60
        self._posY = self._indexY*60
        self._naPolu = naPolu
        if self._naPolu != FLD_EMPTY:
            self.setImage()

    def getIndex(self):
        return self._indexX, self._indexY

    def getPos(self):
        return self._posX, self._posY

    def getNaPolu(self):
        return self._naPolu

    def setNaPolu(self, naPolu):
        self._naPolu = naPolu

