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
        time.sleep(4)  # Ralentir davantage l'attaque, l'exécution du combat
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
        time.sleep(3) #Cette ligne utilise la fonction sleep() du module time pour ralentir l'exécution de la méthode.

    def incremente_combo(self): #Cette ligne définit la méthode incremente_combo() de la classe Combattant.
        self.combo += 5 #Cette ligne augmente la valeur de l'attribut combo de l'objet de 5.
        print(f"{self.symbole} {self.nom} gagne en combo! Chaque attaque normale suivante infligera plus de dégâts.\n")#Cette ligne imprime un message indiquant que le combattant a gagné en combo.

    def reset_combo(self): #Cette ligne définit la méthode reset_combo() de la classe Combattant.
        self.combo = 0 #Cette ligne réinitialise la valeur de l'attribut combo à 0.
        print(f"{self.symbole} {self.nom} perd le combo!\n")

def introduction(): #Cette ligne définit la méthode introduction().
    print("Bienvenue dans le combat à la Street Fighter!") #Cette ligne imprime un message d'introduction.
    time.sleep(3) #Cette ligne utilise la fonction sleep() du module time pour ralentir l'exécution de la méthode.
    print("Deux combattants vont s'affronter dans une bataille épique.") #Cette ligne imprime un message annonçant le combat.
    time.sleep(3) #Cette ligne utilise la fonction sleep() du module time pour ralentir l'exécution de la méthode.
    print("Que le meilleur gagne!\n") #Cette ligne imprime un message de conclusion.

def afficher_combat(combattant1, combattant2): #Cette ligne définit la méthode afficher_combat().
    print(f"{combattant1.symbole} {combattant1.nom} vs {combattant2.symbole} {combattant2.nom}")#Cette ligne imprime un message indiquant les combattants qui s'affrontent.
    print(f"{combattant1.symbole} Points de vie : {combattant1.points_de_vie}") #Cette ligne imprime le nombre de points de vie du combattant 1.
    print(f"{combattant2.symbole} Points de vie : {combattant2.points_de_vie}\n") #Cette ligne imprime le nombre de points de vie du combattant 2.

def resumer_manche(num_manche, combattant1, combattant2):#Cette ligne définit la méthode resumer_manche().
    print(f"\nDébut de la manche {num_manche}!") #Cette ligne imprime un message annonçant le début d'une manche.
    time.sleep(3) #Cette ligne utilise la fonction sleep() du module time pour ralentir l'exécution de la méthode.
    afficher_combat(combattant1, combattant2) #Cette ligne appelle la méthode afficher_combat() pour afficher l'état des combattants au début de la manche

    while combattant1.points_de_vie > 0 and combattant2.points_de_vie > 0: #Cette ligne commence une boucle while qui continue tant que les deux combattants ont encore des points de vie.
        # Choix aléatoire de l'attaque
        attaque_combattant1 = random.choice([True, False]) #Cette ligne génère un nombre aléatoire entre 0 et 1. Si le nombre est inférieur à 0,5, la valeur de la variable attaque_combattant1 est True. Sinon, elle est False.
        attaque_combattant2 = random.choice([True, False]) #Cette ligne est similaire à la ligne précédente, mais elle génère un nombre aléatoire pour la variable attaque_combattant2.

        # Attaque du combattant 1
        combattant1.attaquer(combattant2, attaque_combattant1) #Cette ligne appelle la méthode attaquer() du combattant 1 en lui passant l'objet combattant2 et la valeur de la variable attaque_combattant1.
        afficher_combat(combattant1, combattant2) #Cette ligne appelle la méthode afficher_combat() pour afficher l'état des combattants après l'attaque du combattant 1.
        if combattant2.points_de_vie <= 0:#Cette ligne teste si le combattant 2 a encore des points de vie. Si ce n'est pas le cas, la boucle while est interrompue.
            break  # Sortir de la boucle si le combattant 2 est KO

        # Attaque du combattant 2
        combattant2.attaquer(combattant1, attaque_combattant2) #Cette ligne est similaire à la ligne 61, mais elle représente l'attaque du combattant 2.
        afficher_combat(combattant1, combattant2) #Cette ligne est similaire à la ligne 62, mais elle affiche l'état des combattants après l'attaque du combattant 2.
        if combattant1.points_de_vie <= 0: #Cette ligne est similaire à la ligne 63.
            break  # Sortir de la boucle si le combattant 1 est KO

    print(f"Fin de la manche {num_manche}!") #Cette ligne imprime un message annonçant la fin d'une manche.
    time.sleep(3) #Cette ligne utilise la fonction sleep() pour ralentir l'exécution du programme.

def resumer_combat(combattant1, combattant2): #Cette ligne définit la fonction resumer_combat(), qui résume le combat entre deux combattants.
    print("\nRésumé du combat :") #Cette ligne imprime un message annonçant le résumé du combat.
    time.sleep(3) #Cette ligne utilise la fonction sleep() pour ralentir l'exécution du programme.
    afficher_combat(combattant1, combattant2) #Cette ligne appelle la fonction afficher_combat(), qui affiche l'état des combattants.
    time.sleep(4) #Cette ligne utilise la fonction sleep() pour ralentir l'exécution du programme.
    if combattant1.points_de_vie > combattant2.points_de_vie: #Cette ligne teste si le combattant 1 a plus de points de vie que le combattant 2.
        print(f"{combattant1.symbole} {combattant1.nom} remporte le combat!") #Cette ligne imprime un message indiquant que le combattant 1 a remporté le combat.
    elif combattant2.points_de_vie > combattant1.points_de_vie: #Cette ligne est similaire à la ligne 6, mais elle teste si le combattant 2 a plus de points de vie que le combattant 1.
        print(f"{combattant2.symbole} {combattant2.nom} remporte le combat!") #Cette ligne est similaire à la ligne 7, mais elle indique que le combattant 2 a remporté le combat.
    else: #Cette ligne est exécutée si aucune des conditions des lignes 6 ou 8 n'est remplie.
        print("Le combat se termine par un match nul.") #Cette ligne imprime un message indiquant que le combat s'est terminé par un match nul.

def combat(): #Cette ligne définit la fonction combat(), qui lance le combat.
    introduction() #Cette ligne appelle la fonction introduction(), qui affiche un message d'introduction au combat.

    # Création des combattants avec des symboles
    combattant1 = Combattant("Ryu", 100, 10, 20, "🥋") #Cette ligne crée le combattant 1 avec le nom "Ryu", 100 points de vie, une attaque normale de 10 et une attaque spéciale de 20. Le symbole du combattant est "🥋".
    combattant2 = Combattant("Ken", 100, 12, 18, "🔥") #Cette ligne est similaire à la ligne 15, mais elle crée le combattant 2 avec le nom "Ken".

    resumer_manche(1, combattant1, combattant2) #Cette ligne appelle la fonction resumer_manche(), qui lance une manche du combat.

    resumer_combat(combattant1, combattant2) #Cette ligne appelle la fonction resumer_combat(), qui résume le combat.

# Début du combat
combat() #Cette ligne appelle la fonction combat(), qui lance le combat.
