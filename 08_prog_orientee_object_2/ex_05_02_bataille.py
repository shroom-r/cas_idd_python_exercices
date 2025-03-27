import random
from collections import deque

COULEUR = ("Pique", "Coeur", "Carreau", "Trèfle")
VALEUR = (
    "Deux",
    "Trois",
    "Quatre",
    "Cinq",
    "Six",
    "Sept",
    "Huit",
    "Neuf",
    "Dix",
    "Valet",
    "Dame",
    "Roi",
    "As",
)

class Carte:
    def __init__(self, valeur, couleur):
        if valeur == 1:
            # Cas de l'As
            valeur = 14
        self.valeur = valeur

        self.couleur = couleur

    def __repr__(self):
        return VALEUR[self.valeur - 2] + ' de ' + self.couleur
    
    def __gt__(self, c2):
        return self.valeur > c2.valeur
    
    def __lt__(self, c2):
        return self.valeur < c2.valeur
    
class Jeu:
    def __init__(self):
        self.cartes = deque([])
        for coul in COULEUR:
            for val in range(1,14):
                self.cartes.append(Carte(val, coul))
    
    def melange(self):
        random.shuffle(self.cartes)
    
    def add(self, cartes):
        self.cartes.extendleft(cartes)

    def tire(self):
        return self.cartes.pop()

    def __iter__(self):
        return self.cartes
    
class Joueur:
    def __init__(self, name):
        self.name = name
        self.jeu = Jeu()
        self.jeu.melange()
        self.points = 0

    def joue(self):
        return self.jeu.tire()

def run_game():
    j1 = Joueur("Aline")
    j2 = Joueur("Bette")

    pile1 = []
    pile2 = []
    while j1.jeu.cartes:
        
        c1 = j1.joue()
        c2 = j2.joue()
        pile1.append(c1)
        pile2.append(c2)
        print(f'{j1.name:} {c1}')
        print(f'{j2.name:} {c2}')
        if c1 > c2:
            print(f'{j1.name} gagne!')
            j1.points+=1
            j1.jeu.add(pile1 + pile2)
        elif c2 > c1:
            print(f'{j2.name} gagne!')
            j2.points+=1
            j2.jeu.add(pile1 + pile2)
        else:
            # Bataille case
            continue
            print("Egalité, aucun point attribué")
        print(f'Score: {j1.name}: {j1.points} - {j2.name}: {j2.points}')
        print("")
        pile1 = []
        pile2 = []

if __name__ == "__main__":
    run_game()