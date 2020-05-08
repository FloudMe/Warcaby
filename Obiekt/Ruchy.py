from Plansza.Constant import *

def ruchyOrazBicia(szachownica, pole):  # zwraca słownik dict[docelowy_cord] = zbity_pion
    polaPuste = pionki(szachownica, FLD_EMPTY)
    return_dict = ruchy(pole, polaPuste)
    return_dict.update(bicia(szachownica, pole, polaPuste))
    return return_dict

def ruchy(pole, polaPuste):
    return_dict = dict()
    x, y = pole.getIndex()
    if pole.getNaPolu() == FLD_WHITE:
        if (x - 1, y - 1) in polaPuste:
            if x - 1 >= 0 and y + 1 <= 7:
                return_dict[(x - 1, y - 1)] = 0

        if (x + 1, y - 1) in polaPuste:
            if x + 1 <= 7 and y + 1 <= 7:
                return_dict[(x + 1, y - 1)] = 0

    elif pole.getNaPolu() == FLD_BLACK:
        if (x - 1, y + 1) in polaPuste:
            if x - 1 >= 0 and y - 1 >= 0:
                return_dict[(x - 1, y + 1)] = 0

        if (x + 1, y + 1) in polaPuste:
            if x + 1 <= 7 and y - 1 >= 0:
                return_dict[(x + 1, y + 1)] = 0
    return return_dict

def bicia(szachownica, pole, polaPuste):
    przeciwnik = -1
    return_dict = dict()
    if pole.getNaPolu == FLD_WHITE:
        przeciwnik = FLD_BLACK
    elif pole.getNaPolu == FLD_BLACK:
        przeciwnik = FLD_WHITE
    else:
        return return_dict
    polaPrzeciwnikow = pionki(szachownica, przeciwnik)


    x, y = pole.getIndex()
    if (x - 1, y - 1) in polaPrzeciwnikow and (x - 2, y - 2) in polaPuste:
        if x - 2 >= 0 and y - 2 >= 0:
            return_dict[(x - 2, y - 2)] = (x - 1, y - 1)

    if (x + 1, y - 1) in polaPrzeciwnikow and (x + 2, y - 2) in polaPuste:
        if x + 2 <= 7 and y - 2 >= 0:
            return_dict[(x + 2, y - 2)] = (x + 1, y - 1)

    if (x - 1, y + 1) in polaPrzeciwnikow and (x - 2, y + 2) in polaPuste:
        if x - 2 >= 0 and y - 2 <= 7:
            return_dict[(x - 2, y + 2)] = (x - 1, y + 1)

    if (x + 1, y + 1) in polaPrzeciwnikow and (x + 2, y + 2) in polaPuste:
        if x + 2 <= 7 and y + 2 <= 7:
            return_dict[(x + 2, y + 2)] = (x + 1, y + 1)
    return return_dict

def pionki(szachownica, field):
    pola = []
    for i in range(8):
        for j in range(8):
            if szachownica.getCurrentField(i, j).getNaPolu() == field:
                pola.append((i, j))
    return pola
