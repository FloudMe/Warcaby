import os

import pygame

from Obiekt.Ruchy import ruchyOrazBicia
from Plansza.Constant import *


class Pole:
    def __init__(self, x, y, naPolu):
        self._indexX = x
        self._indexY = y
        self._posX = self._indexX*FLD
        self._posY = self._indexY*FLD
        self._tempPosX = self._posX
        self._tempPosY = self._posY
        self._naPolu = naPolu
        self._ruchy = dict()
        self._iloscRuchow = 0
        self._iloscBic = 0

    def getIndex(self):
        return self._indexX, self._indexY

    def getPos(self):
        return self._posX, self._posY

    def setTempPos(self, x, y):
        self._posX = x - (FLD/2)
        self._posY = y - (FLD/2)

    def setTemp(self):
        self._posX, self._posY = self._tempPosX, self._tempPosY

    def getNaPolu(self):
        return self._naPolu

    def setNaPolu(self, naPolu):
        self._naPolu = naPolu

    def setRuchy(self, szachownica):
        self._ruchy = dict()
        self._ruchy = ruchyOrazBicia(szachownica, self)
        self._iloscRuchow = len(self._ruchy)
        self._iloscBic = 0
        for key, value in self._ruchy.items():
            if value != 0:
                self._iloscBic +=1

    def getRuchy(self):
        return self._ruchy

    def getIloscRuchow(self):
        return self._iloscRuchow

    def getIloscBic(self):
        return self._iloscBic
