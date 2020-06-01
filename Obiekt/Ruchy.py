from Plansza.Constant import FLD_EMPTY, FLD_WHITE, FLD_BLACK, FLD_WHITE_DAMKA, FLD_BLACK_DAMKA

def ruchyOrazBicia(szachownica, pole):  # zwraca słownik dict[docelowy_cord] = zbity_pion
    polaPuste = pionki(szachownica, FLD_EMPTY)
    return_dict = ruchy(pole, polaPuste)
    return_dict.update(bicia(szachownica, pole, polaPuste))
    return return_dict

def ruchy(pole, polaPuste):
    return_dict = dict()
    x, y = pole.indexX, pole.indexY
    if pole.naPolu == FLD_WHITE:
        if (x - 1, y - 1) in polaPuste:
            return_dict[(x - 1, y - 1)] = 0

        if (x + 1, y - 1) in polaPuste:
            return_dict[(x + 1, y - 1)] = 0

    elif pole.naPolu == FLD_BLACK:
        if (x - 1, y + 1) in polaPuste:
            return_dict[(x - 1, y + 1)] = 0

        if (x + 1, y + 1) in polaPuste:
            return_dict[(x + 1, y + 1)] = 0
    elif pole.naPolu == FLD_WHITE_DAMKA or pole.naPolu == FLD_BLACK_DAMKA:
        #w gore
        for j in range(1, 8):
            if (x, y - j) in polaPuste:
                return_dict[(x, y - j)] = 0
            else:
                break
        #w dol
        for j in range(1, 8):
            if (x, y + j) in polaPuste:
                return_dict[(x, y + j)] = 0
            else:
                break
        #w prawo
        for j in range(1, 8):
            if (x + j, y ) in polaPuste:
                return_dict[(x + j, y)] = 0
            else:
                break
        #w lewo
        for j in range(1, 8):
            if (x - j, y) in polaPuste:
                return_dict[(x - j, y)] = 0
            else:
                break
        #przekatna polnocny wschod
        for j in range(1, 8):
            if (x + j, y - j) in polaPuste:
                return_dict[(x + j, y - j)] = 0
            else:
                break
        #przekatna poludniowy zachod
        for j in range(1, 8):
            if (x - j, y + j) in polaPuste:
                return_dict[(x - j, y + j)] = 0
            else:
                break
        #przekatna polnocny zachod
        for j in range(1, 8):
            if (x - j, y - j) in polaPuste:
                return_dict[(x - j, y - j)] = 0
            else:
                break
        #przekatna poludniowy wschod
        for j in range(1, 8):
            if (x + j, y + j) in polaPuste:
                return_dict[(x + j, y + j)] = 0
            else:
                break
    return return_dict

def bicia(szachownica, pole, polaPuste):
    przeciwnik = -1
    return_dict = dict()
    if pole.naPolu in [FLD_WHITE, FLD_WHITE_DAMKA]:
        przeciwnik = FLD_BLACK
    elif pole.naPolu in [FLD_BLACK, FLD_BLACK_DAMKA]:
        przeciwnik = FLD_WHITE
    else:
        return return_dict

    polaPrzeciwnikow = pionki(szachownica, przeciwnik)

    x, y = pole.indexX, pole.indexY

    if pole.naPolu in [FLD_WHITE, FLD_BLACK]:
        if (x - 1, y - 1) in polaPrzeciwnikow and (x - 2, y - 2) in polaPuste:
            return_dict[(x - 2, y - 2)] = (x - 1, y - 1)

        if (x + 1, y - 1) in polaPrzeciwnikow and (x + 2, y - 2) in polaPuste:
            return_dict[(x + 2, y - 2)] = (x + 1, y - 1)

        if (x - 1, y + 1) in polaPrzeciwnikow and (x - 2, y + 2) in polaPuste:
            return_dict[(x - 2, y + 2)] = (x - 1, y + 1)

        if (x + 1, y + 1) in polaPrzeciwnikow and (x + 2, y + 2) in polaPuste:
            return_dict[(x + 2, y + 2)] = (x + 1, y + 1)

    elif pole.naPolu in [FLD_WHITE_DAMKA, FLD_BLACK_DAMKA]:
        # przekatna polnocny wschod
        for j in range(1, 7):
            if (x + j, y - j) in polaPrzeciwnikow and (x + j + 1, y - j - 1) in polaPuste:
                return_dict[(x + j + 1, y - j - 1)] = (x + j, y - j)
                break
            elif (x + j, y - j) in polaPrzeciwnikow and (x + j + 1, y - j - 1) not in polaPuste:
                break

        # przekatna poludniowy zachod
        for j in range(1, 7):
            if (x - j, y + j) in polaPrzeciwnikow and (x - j - 1, y + j + 1) in polaPuste:
                return_dict[(x - j - 1, y + j + 1)] = (x - j, y + j)
                break
            elif (x - j, y + j) in polaPrzeciwnikow and (x - j - 1, y + j + 1) not in polaPuste:
                break

        # przekatna polnocny zachod
        for j in range(1, 7):
            if (x - j, y - j) in polaPrzeciwnikow and (x - j - 1, y - j - 1) in polaPuste:
                return_dict[(x - j - 1, y - j - 1)] = (x - j, y - j)
                break
            elif (x - j, y - j) in polaPrzeciwnikow and (x - j - 1, y - j - 1) not in polaPuste:
                break
        # przekatna poludniowy wschod
        for j in range(1, 7):
            if (x + j, y + j) in polaPrzeciwnikow and (x + j + 1, y + j + 1) in polaPuste:
                return_dict[(x + j + 1, y + j + 1)] = (x + j, y + j)
                break
            elif (x + j, y + j) in polaPrzeciwnikow and (x + j + 1, y + j + 1) not in polaPuste:
                break
    return return_dict

def pionki(szachownica, field):
    pola = []
    for i in range(8):
        for j in range(8):
            if szachownica.field[i][j].naPolu == field:
                pola.append((i, j))
            if field != FLD_EMPTY and szachownica.field[i][j].naPolu == field + 2:
                pola.append((i, j))
    return pola

