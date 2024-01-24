import time #Cette ligne importe le module time de Python, qui permet de contrôler le temps.
import random #Cette ligne importe le module random de Python, qui permet de générer des nombres aléatoires.

class Combattant: #Définition de la classe Combattant.
    def __init__(self, nom, points_de_vie, attaque_normale, attaque_speciale, symbole): #Cette ligne définit le constructeur de la classe Combattant.
        self.nom = nom #Cette ligne assigne la valeur du paramètre nom à l'attribut nom de l'objet.
        self.points_de_vie = points_de_vie #Cette ligne assigne la valeur du paramètre points_de_vie à l'attribut points_de_vie de l'objet.
        self.attaque_normale = attaque_normale #Cette ligne assigne la valeur du paramètre attaque_normale à l'attribut attaque_normale de l'objet.
        self.attaque_speciale = attaque_speciale #Cette ligne assigne la valeur du paramètre attaque_speciale à l'attribut attaque_speciale de l'objet.
        self.combo = 0 #Cette ligne initialise l'attribut combo de l'objet à 0.
        self.symbole = symbole #Cette ligne assigne la valeur du paramètre symbole à l'attribut symbole de l'objet.

    def attaquer(self, autre_combattant, est_attaque_speciale=False): #Cette ligne définit la méthode attaquer() de la classe Combattant.
        time.sleep(2)  # Ralentir davantage l'attaque, l'exécution du combat
        if est_attaque_speciale: #Cette ligne teste la valeur du paramètre est_attaque_speciale.
            print(f"{self.symbole} {self.nom} lance une attaque spéciale sur {autre_combattant.symbole} {autre_combattant.nom}! 💥") #Cette ligne imprime un message indiquant que le combattant lance une attaque spéciale.
            autre_combattant.subir_attaque(self.attaque_speciale) #Cette ligne appelle la méthode subir_attaque() de l'objet autre_combattant en lui passant l'attaque spéciale du combattant en paramètre.
            self.reset_combo() ##Cette ligne réinitialise la valeur de l'attribut combo à 0.
        else: #Cette ligne exécute le code suivant si la valeur du paramètre est_attaque_speciale est False.
            degats = self.attaque_normale + self.combo #Cette ligne calcule les dégâts infligés par l'attaque normale du combattant.
            print(f"{self.symbole} {self.nom} attaque {autre_combattant.symbole} {autre_combattant.nom} et inflige {degats} points de dégâts. ⚔️") #Cette ligne imprime un message indiquant que le combattant a infligé des dégâts à l'autre combattant.
            autre_combattant.subir_attaque(degats) #Cette ligne appelle la méthode subir_attaque() de l'objet autre_combattant en lui passant les dégâts infligés en paramètre.
            self.incremente_combo() #Cette ligne augmente la valeur de l'attribut combo de 5.

    def subir_attaque(self, degats): #Cette ligne définit la méthode subir_attaque() de la classe Combattant.
        self.points_de_vie -= degats #Cette ligne décrémente la valeur de l'attribut points_de_vie de l'objet de la valeur des dégâts infligés.
        print(f"{self.symbole} {self.nom} perd {degats} points de vie. Points de vie restants : {self.points_de_vie}\n") #Cette ligne imprime un message indiquant que le combattant a perdu des points de vie.
        time.sleep(2) #Cette ligne utilise la fonction sleep() du module time pour ralentir l'exécution de la méthode.

    def incremente_combo(self): #Cette ligne définit la méthode incremente_combo() de la classe Combattant.
        self.combo += 5 #Cette ligne augmente la valeur de l'attribut combo de l'objet de 5.
        print(f"{self.symbole} {self.nom} gagne en combo! Chaque attaque normale suivante infligera plus de dégâts.\n")#Cette ligne imprime un message indiquant que le combattant a gagné en combo.

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
