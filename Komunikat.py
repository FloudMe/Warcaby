import pygame

from Plansza.Constant import FLD_WHITE, FLD_BLACK, FLD_ALL, ROZMIAR_CZCIONKI


def komunikatOPrzegranej(turn, screen, *mouse):
    global player
    if turn == FLD_WHITE:
        player = 'czarny'
    elif turn == FLD_BLACK:
        player = 'bialy'
    screen.fill((0,0,0))


    myfont = pygame.font.SysFont('freesansbold.ttf', ROZMIAR_CZCIONKI)

    textOWygranej = myfont.render('Wygral gracz ' + player, True, (255, 255, 255), (0,0,0))
    textRect = textOWygranej.get_rect()
    textRect.center = (FLD_ALL / 2, FLD_ALL / 2 + ROZMIAR_CZCIONKI / 2)
    screen.blit(textOWygranej, textRect)

    zapytanie = myfont.render('Restart', True, (255, 255, 255), (255,200,0))
    textRect = zapytanie.get_rect()
    textRect.center = (FLD_ALL / 2, FLD_ALL / 2 + ROZMIAR_CZCIONKI * 1.5)

    screen.blit(zapytanie, textRect)
    if pygame.mouse.get_pressed()[0] and textRect[0] < mouse[0] < textRect[0] + textRect[2] and textRect[1] < mouse[1] < textRect[1] + textRect[3]:
        return True
    return False


def turaGracza(turn, screen):
    global player
    if turn == FLD_WHITE:
        player = 'bialymi'
    elif turn == FLD_BLACK:
        player = 'czarnymi'

    myfont = pygame.font.Font('freesansbold.ttf', ROZMIAR_CZCIONKI)
    text = myfont.render('Tura gracza z pionkami: ' + player, True, (255, 255, 255), (0,0,0))
    textRect = text.get_rect()
    textRect.center = (FLD_ALL/2, FLD_ALL + ROZMIAR_CZCIONKI/2)
    screen.blit(text, textRect)