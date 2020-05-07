from Plansza import Pole
from Plansza.Constant import *


class Szachownica:
    def __init__(self):
        self._field = self.setList()

    def setList(self):
        for i in range(10):
            for j in range(10):
                self._field.append(Pole(i, j, FLD_EMPTY))
        for i in range(5):
            for j in range(3):
                self._field.append(Pole(i * 2 + j % 2, j, FLD_WHITE))
        for i in range(5):
            for j in range(3):
                self._field.append(Pole(1 + i * 2 - j % 2, 9 - j, FLD_BLACK))

    def getList(self, i, j):
        return self._field[i,j].getNaPolu()

    def naPionku(self, mouse):
        for pole in self._field:
            x, y = pole.getPos()
            if mouse[0] > x and x + 60 > mouse[0] and mouse [1] > y and y + 60 > mouse[1]:
                return True, pole
            return False


