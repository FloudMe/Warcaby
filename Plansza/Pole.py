from Obiekt.Ruchy import ruchyOrazBicia
from Plansza.Constant import FLD


class Pole:
    def __init__(self, x, y, naPolu):
        self.indexX = x
        self.indexY = y
        self.posX = self.indexX*FLD
        self.posY = self.indexY*FLD
        self.tempPosX = self.posX
        self.tempPosY = self.posY
        self.naPolu = naPolu
        self.ruchy = dict()
        self.iloscRuchow = 0
        self.iloscBic = 0

    def setRuchy(self, szachownica):
        self.ruchy = dict()
        self.ruchy = ruchyOrazBicia(szachownica, self)
        self.iloscRuchow = len(self.ruchy)
        self.iloscBic = 0
        for key, value in self.ruchy.items():
            if value != 0:
                self.iloscBic +=1
