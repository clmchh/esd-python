import time
import random

class Combattant:
    def __init__(self, nom, points_de_vie, attaque_normale, attaque_speciale, symbole):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.attaque_normale = attaque_normale
        self.attaque_speciale = attaque_speciale
        self.combo = 0
        self.symbole = symbole

    def attaquer(self, autre_combattant, est_attaque_speciale=False):
        time.sleep(2)  # Ralentir davantage l'attaque
        if est_attaque_speciale:
            print(f"{self.symbole} {self.nom} lance une attaque spéciale sur {autre_combattant.symbole} {autre_combattant.nom}! 💥")
            autre_combattant.subir_attaque(self.attaque_speciale)
            self.reset_combo()
        else:
            degats = self.attaque_normale + self.combo
            print(f"{self.symbole} {self.nom} attaque {autre_combattant.symbole} {autre_combattant.nom} et inflige {degats} points de dégâts. ⚔️")
            autre_combattant.subir_attaque(degats)
            self.incremente_combo()

    def subir_attaque(self, degats):
        self.points_de_vie -= degats
        print(f"{self.symbole} {self.nom} perd {degats} points de vie. Points de vie restants : {self.points_de_vie}\n")
        time.sleep(2)

    def incremente_combo(self):
        self.combo += 5
        print(f"{self.symbole} {self.nom} gagne en combo! Chaque attaque normale suivante infligera plus de dégâts.\n")

    def reset_combo(self):
        self.combo = 0
        print(f"{self.symbole} {self.nom} perd le combo!\n")

def introduction():
    print("Bienvenue dans le combat à la Street Fighter!")
    time.sleep(3)
    print("Deux combattants vont s'affronter dans une bataille épique.")
    time.sleep(3)
    print("Que le meilleur gagne!\n")

def afficher_combat(combattant1, combattant2):
    print(f"{combattant1.symbole} {combattant1.nom} vs {combattant2.symbole} {combattant2.nom}")
    print(f"{combattant1.symbole} Points de vie : {combattant1.points_de_vie}")
    print(f"{combattant2.symbole} Points de vie : {combattant2.points_de_vie}\n")

def resumer_manche(num_manche, combattant1, combattant2):
    print(f"\nDébut de la manche {num_manche}!")
    time.sleep(3)
    afficher_combat(combattant1, combattant2)

    while combattant1.points_de_vie > 0 and combattant2.points_de_vie > 0:
        # Choix aléatoire de l'attaque
        attaque_combattant1 = random.choice([True, False])
        attaque_combattant2 = random.choice([True, False])

        # Attaque du combattant 1
        combattant1.attaquer(combattant2, attaque_combattant1)
        afficher_combat(combattant1, combattant2)
        if combattant2.points_de_vie <= 0:
            break  # Sortir de la boucle si le combattant 2 est KO

        # Attaque du combattant 2
        combattant2.attaquer(combattant1, attaque_combattant2)
        afficher_combat(combattant1, combattant2)
        if combattant1.points_de_vie <= 0:
            break  # Sortir de la boucle si le combattant 1 est KO

    print(f"Fin de la manche {num_manche}!")
    time.sleep(3)

def resumer_combat(combattant1, combattant2):
    print("\nRésumé du combat :")
    time.sleep(3)
    afficher_combat(combattant1, combattant2)
    time.sleep(3)
    if combattant1.points_de_vie > combattant2.points_de_vie:
        print(f"{combattant1.symbole} {combattant1.nom} remporte le combat!")
    elif combattant2.points_de_vie > combattant1.points_de_vie:
        print(f"{combattant2.symbole} {combattant2.nom} remporte le combat!")
    else:
        print("Le combat se termine par un match nul.")

def combat():
    introduction()

    # Création des combattants avec des symboles
    combattant1 = Combattant("Ryu", 100, 10, 20, "🥋")
    combattant2 = Combattant("Ken", 100, 12, 18, "🔥")

    resumer_manche(1, combattant1, combattant2)

    resumer_combat(combattant1, combattant2)

# Début du combat
combat()
