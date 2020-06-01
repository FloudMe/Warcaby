import Funkcje
from Plansza.Pole import Pole
from Plansza.Constant import FLD_EMPTY, FLD_BLACK, FLD_WHITE, FLD_WHITE_DAMKA, FLD_BLACK_DAMKA, FLD


class Szachownica:
    def __init__(self):
        self.field = [[Pole(i,j, FLD_EMPTY) for j in range(8)] for i in range(8)]
        self.setList()

    def setList(self):
        for i in range(4):
            for j in range(3):
                x = 1 + i * 2 - j % 2
                y = j
                self.field[x][y].naPolu = FLD_BLACK

        for i in range(4):
            for j in range(3):
                x = i * 2 + j % 2
                y = 7 - j
                self.field[x][y].naPolu = FLD_WHITE

    def getListaPol(self):
        listBiale = []
        listCzarne = []
        listDamkaBiala = []
        listDamkaCzarna = []

        for i in range(8):
            for j in range(8):
                pole = self.field[i][j]
                naPolu = pole.naPolu

                if naPolu != FLD_EMPTY:
                    if naPolu == FLD_WHITE:
                        listBiale.append(pole)
                    elif naPolu == FLD_BLACK:
                        listCzarne.append(pole)
                    elif naPolu == FLD_WHITE_DAMKA:
                        listDamkaBiala.append(pole)
                    elif naPolu == FLD_BLACK_DAMKA:
                        listDamkaCzarna.append(pole)
                    pole.setRuchy(szachownica=self)

        return listBiale, listCzarne, listDamkaBiala, listDamkaCzarna

    def naPionku(self, *mouse, screen, turn):
        for raw in self.field:
            for pole in raw:
                x, y = pole.posX, pole.posY
                if (pole.naPolu == turn or pole.naPolu == turn + 2) and x < mouse[0] < x + FLD and y < mouse [1] < y + FLD:
                    Funkcje.draw(x, y, screen, 'podswietlenie.png')
                    return pole
        return

    def getIloscBicNaPlanszy(self):
        iloscBicBialych, iloscBicCzarnych  = 0, 0

        for row in self.field:
            for field in row:
                if field.naPolu in [FLD_WHITE, FLD_WHITE_DAMKA]:
                    iloscBicBialych += field.iloscBic
                elif field.naPolu in [FLD_BLACK, FLD_BLACK_DAMKA]:
                    iloscBicCzarnych += field.iloscBic
        return iloscBicBialych, iloscBicCzarnych

    def getIloscRuchowNaPlanszy(self):
        iloscRuchowBialych, iloscRuchowCzarnych = 0, 0
        for row in self.field:
            for field in row:
                if field.naPolu in [FLD_WHITE, FLD_WHITE_DAMKA]:
                    iloscRuchowBialych += field.iloscRuchow
                elif field.naPolu in [FLD_BLACK, FLD_BLACK_DAMKA]:
                    iloscRuchowCzarnych += field.iloscRuchow
        return iloscRuchowBialych, iloscRuchowCzarnych



