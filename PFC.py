from random import*

def bat(j1, j2):
    return (j1 - j2) % 3 == 1


s = int(input())
seed(s)

x = 0
PIERRE = 0
FEUILLE = 1
CISEAUX = 2
resultat = 0

while x < 5:
    x += 1
    coup_o = randint(0, 2)
    coup_j = int(input())

    if bat(coup_o, coup_j):
        resultat -= 1
        if coup_o == 0 and coup_j == 2:
            print(f"Pierre bat Ciseaux : {resultat}")
        elif coup_o == 1 and coup_j == 0:
            print(f"Feuille bat Pierre : {resultat}")
        elif coup_o == 2 and coup_j == 1:
            print(f"Ciseaux bat Feuille : {resultat}")
    elif coup_o == coup_j:
        if coup_o == 0:
            print(f"Pierre annule Pierre : {resultat}")
        elif coup_o == 1:
            print(f"Feuille annule Feuille : {resultat}")
        elif coup_o == 2:
            print(f"Ciseaux annule Ciseaux : {resultat}")

    elif bat(coup_o, coup_j) != True:
        resultat += 1
        if coup_o == 0 and coup_j == 1:
            print(f"Pierre est battu par Feuille : {resultat}")
        elif coup_o == 1 and coup_j == 2:
            print(f"Feuille est battu par Ciseaux : {resultat}")
        elif coup_o == 2 and coup_j == 0:
            print(f"Ciseaux est battu par Pierre : {resultat}")

if resultat == 0:
    print("Nul")
elif resultat > 0:
    print("Gagné")
else:
    print("Perdu")