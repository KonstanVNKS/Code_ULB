# imports
from math import sqrt
from random import randint, seed



def roullette(pari: int, somme:int):
    pari_joueur = pari
    numero_tirage = somme
    red = [1,3,5,7,9,12]
    black =[2,4,6,8,10,11]

    # Vérifier le type de pari et calculer le montant gagné par le joueur
    montant_gagne = 10

    if 0 <= pari_joueur <= 12:
        # Le joueur a parié sur un numéro
        if pari_joueur == numero_tirage:
            montant_gagne = 10*12  # Le joueur gagne 36 fois sa mise
        else:
            montant_gagne = 0
    else:
        if pari_joueur == 13:
            # Le joueur a parié sur pair
            if numero_tirage % 2 == 0:
                montant_gagne = 10*2  # Le joueur gagne deux fois sa mise
            else:
                montant_gagne = 0
        elif pari_joueur == 14:
            # Le joueur a parié sur impair
            if numero_tirage % 2 != 0:
                montant_gagne = 10*2  # Le joueur gagne deux fois sa mise
            else:
                montant_gagne = 0
        elif pari_joueur == 15:
            # Le joueur a parié sur la couleur rouge (supposons que la couleur rouge correspond aux numéros pairs)
            if numero_tirage in red:
                montant_gagne = 10*2  # Le joueur gagne deux fois sa mise
            else:
                montant_gagne = 0
        elif pari_joueur == 16:
            # Le joueur a parié sur la couleur noire (supposons que la couleur noire correspond aux numéros impairs)
            if numero_tirage in black:
                montant_gagne = 10*2  # Le joueur gagne deux fois sa mise
            else:
                montant_gagne = 0
    return montant_gagne





def devine(choix: int):
    ESSAIS_MAX = 6
    number = randint(0, 100)
    count = 0
    guess = choix

    while count < ESSAIS_MAX and guess != number:
        if guess > number:
            print("Trop grand")
            count += 1
            guess = int(input())
        elif guess < number:
            print("Trop petit")
            count +=1
            guess = int(input())
    if guess == number:
        print('Gagné en {0} essai(s) !'.format(count))
        win = True
    elif count == ESSAIS_MAX:
        print('Perdu ! Le secret était nombre {0} '.format(number))
        win = True
    return win


def lapin(saut: int, pos_cible: int):
    pos_courante = 0
    find = False

    while not find:
        pos_courante += saut
        pos_courante %= 100
        print(pos_courante)
        if pos_courante == pos_cible:
            find = True
            print("Cible atteinte")
        elif pos_courante == 0:
            find = True
            print('Pas trouvée')

    return find





def alea_dice(s):
    seed(s)
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    d3 = randint(1, 6)

    return (d1, d2, d3) == (4, 2, 1) or (d1, d2, d3) == (2, 4, 1) or (d1, d2, d3) == (1, 4, 2) or (d1, d2, d3) == (
    2, 1, 4) or (d1, d2, d3) == (4, 1, 2) or (d1, d2, d3) == (1, 2, 4)


def rendre_monnaie(prix, x, y, z, a, b):
    argent = 20*x+10*y+5*z+2*a+b
    dif = argent - prix
    if dif < 0:
        return None, None, None, None, None
    a, b, c, d, e = 0, 0, 0, 0, 0
    if dif >= 20:
        a += (dif//20)
        dif -= (dif//20)*20
    if dif >= 10:
        b += (dif//10)
        dif -= (dif//10)*10
    if dif >= 5:
        c += (dif//5)
        dif -= (dif//5)*5
    if dif >= 2:
        d += (dif//2)
        dif -= (dif//2)*2
    if dif >= 1:
        e += dif
        dif -= dif
    return a, b, c, d, e




