import random

def ppc():
    scoreUser = 0
    scoreProg = 0
    print()
    nbPartie = int(input("Combien de partie souhaitez-vous jouer? "))
    while nbPartie <= 0:
        nbPartie = int(input("Erreur, le nombre de partie que vous avez entrés est égal à 0 ou est un nombre négatif, veuillez réessayez"))
    for i in range(nbPartie):
        choixUser = input("Que choisissez-vous, pierre, papier ou ciseau?")
        choixProg = range.randint(1, 3)
        if (choixUser.upper() == "PIERRE" and choixProg == 3) or (choixUser.upper() == "PAPIER" and choixProg == 1) or (choixUser.upper() == "CISEAU" and choixProg == 2):
            print(f"Vous avez gagné! ")
