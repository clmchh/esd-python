A FAIRE : TOUT METTRE SOUS FORME DE FONCTION....

#Fonction "multiplie" qui multiplie deux nombres en paramètre par additions successives.

def multiplie (a,b): #multiplication de 2 nombres (a et b) par additions successives
    resultat=0
    for i in range(b):
        resultat+=a
    return resultat

>>> resultat = 0
>>> for i in range (7):
...     resultat+=4
... 
>>> print(resultat)
28
>>> 
>>> 
>>> #Fonction "puissance" qui calcule les puissances par multiplication successives.
>>> 
>>> def puissance (a,n):
...     resultat=1
...     for i in range(n):
...         resultat*=a
...     return resultat
... 
>>> resultat=1
>>> for i in range(4)
SyntaxError: incomplete input
>>> resultat=1
>>> for i in range(4):
...     resultat*=2
... 
...     
>>> print(resultat)
16


# Demande à l'utilisateur un nombre entier N
n = int(input("Choisissez un nombre entier N : "))

# Initialisation de la somme à 0
somme = 0

# Boucle "for" sur les nombres de 1 à N
for i in range(1, n + 1):
    somme += i

# Affiche la somme
print("La somme des nombres de 1 à N est", somme)

#Exemple : 

n=int(input("Choisissez un nombre entier N:"))
Choisissez un nombre entier N:5
somme=0
for i in range (1,n+1):
    somme +=i

    
print("La somme des nombre de 1 à N correspond à",somme)
La somme des nombre de 1 à N correspond à 15


# Demande à l'utilisateur un nombre entier N
n = int(input("Choisissez un nombre entier N : "))

# Affiche la table de multiplication de N avec une boucle "for"
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

#Exemple : 
n=int(input("Choisissez un nombre entier N:"))
Choisissez un nombre entier N:4
for i in range(1,11):
    print(f"{n} x {i} = {n * i}")

    
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40


# Affiche les nombres de 1 à 10 et indique si chaque nombre est pair ou impair
for i in range(1, 11):
    # Indique si le nombre est pair
    if i % 2 == 0:
        print(f"{i} est pair")
    # Indique si le nombre est impair
    else:
        print(f"{i} est impair")
        
1 est impair
2 est pair
3 est impair
4 est pair
5 est impair
6 est pair
7 est impair
8 est pair
9 est impair
10 est pair


# Demande à l'utilisateur un nombre entier N
n = int(input("Choisissez un nombre entier N : "))

# Initialisation de la la factorielle à 1
factorielle = 1

# Boucle sur les nombres de 1 à N avec une boucle "for"
for i in range(1, n + 1):
    # Multiplie la factorielle par le nombre courant
    factorielle *= i

# Affiche la factorielle
print(f"La factorielle de N est {factorielle}")

#Exemple

n=int(input("Choisissez un nombre entier N:"))
Choisissez un nombre entier N:10
factorielle=1
for i in range (1,n+1):
    factorielle *=i

    
print(f"La factorielle de N est, {factorielle}")
La factorielle de N est, 3628800

# Fonction qui vérifie si un mot est un palindrome
def est_palindrome(mot):
    # Initialisation de la position du début et de la fin du mot
    debut = 0
    fin = len(mot) - 1  # len() renvoie le nombre des éléments (ou la longueur) dans un objet. 

    # Tant que le début et la fin ne se sont pas rencontrés
    while debut < fin:
        # Si les caractères ne sont pas les mêmes
        if mot[debut] != mot[fin]:    # "!=" est utilisé pour vérifier si deux valeurs sont différentes.
            return False

        # Incrémente le début et décrémente la fin
        debut += 1
        fin -= 1

    # Si le début et la fin se sont rencontrés
    return True

# Demande à l'utilisateur un mot
mot = input("Entrez un mot : ")

# Vérifie si le mot est un palindrome
if est_palindrome(mot):
    print("Le mot est un palindrome.")
else:
    print("Le mot n'est pas un palindrome.")

A FAIRE : TOUT METTRE SOUS FORME DE FONCTION....

EXERCICE LISTE CHAPITRE 4

maListe=[3, 7, 12, 22, 30]
maListe.append(8)
maListe.extend ([4, 9])

print("Liste avant le tri:", maListe)
Liste avant le tri: [3, 7, 12, 22, 30, 8, 4, 9]
maListe.sort()

print("Liste triée:", maListe)
Liste triée: [3, 4, 7, 8, 9, 12, 22, 30]

EXERCICE DICTIONNAIRE CHAPITRE 4

monDictionnaire={
    "nom": "Clément Chevallier",
    "âge": 23,
    "adresse": "9bis Rue Montesquieu, La Rochelle, 17000"
}

print("Nom :", monDictionnaire["nom"])
Nom : Clément Chevallier
print("Âge :", monDictionnaire["âge"])
Âge : 23
print("Adresse :", monDictionnaire["adresse"])
Adresse : 9bis Rue Montesquieu, La Rochelle, 17000


EXERCICE 3 UNION INTERSECTION CHAPITRE 4
monEnsemble={1, 2, 3, 4}
monEnsmble={5, 6, 7, 8}

print("Ensemble:", monEnsemble)
Ensemble: {1, 2, 3, 4}
print("Ensemble2:", monEnsemble2)
Ensemble2: {8, 5, 6, 7}

union=monEnsemble.union(monEnsemble2)
print("Union des ensembles":union)
SyntaxError: invalid syntax
print("Union des ensembles":,union)
SyntaxError: invalid syntax
print("Union des ensemble:",union)
Union des ensemble: {1, 2, 3, 4, 5, 6, 7, 8}

intersection=monEnsemble.intersection(monEnsemble2)
print("Intersection des ensembles:",intersection)
Intersection des ensembles: set()

intersection=monEnsemble.intersection(monEnsemble2)
print("Intersection des ensembles:",intersection)
Intersection des ensembles: set()

EXERCICE 1 PRODUIT CHAPITRE 5
def produit(a,b):
    return a*b

print(produit(2,3))
6

EXERCICE 2 PRODUIT CHAPITRE 5
def moyenne (a,b,c):
    return(a+b+c)/3

print(moyenne(2,3,4))
3.0


EXERCICE CONTACT

# Dictionnaire qui stocke les contacts
contacts = {}

# Fonction qui ajoute un contact
def ajouter_contact(nom, numero):
    contacts[nom] = numero

# Fonction qui supprime un contact
def supprimer_contact(nom):
    del contacts[nom]

# Fonction qui recherche un contact
def rechercher_contact(nom):
    if nom in contacts:
        return contacts[nom]
    else:
        return None

# Menu principal
while True:
    print("Que voulez-vous faire ?")
    print("1. Ajouter un contact")
    print("2. Supprimer un contact")
    print("3. Rechercher un contact")
    print("4. Quitter")

    choix = input("Votre choix : ")

    # Traitement du choix de l'utilisateur
    if choix == "1":
        # Demande du nom du contact
        nom = input("Nom du contact : ")

        # Demande du numéro de téléphone du contact
        numero = input("Numéro de téléphone du contact : ")

        # Ajout du contact dans le dictionnaire
        ajouter_contact(nom, numero)

    elif choix == "2":
        # Demande du nom du contact à supprimer
        nom = input("Nom du contact à supprimer : ")

        # Suppression du contact du dictionnaire
        supprimer_contact(nom)

    elif choix == "3":
        # Demande du nom du contact à rechercher
        nom = input("Nom du contact à rechercher : ")

        # Recherche du contact dans le dictionnaire
        numero = rechercher_contact(nom)

        # Affichage du résultat de la recherche
        if numero is not None:
            print("Le numéro de téléphone du contact est :", numero)
        else:
            print("Le contact n'est pas trouvé.")

    elif choix == "4":
        # Quitter le programme
        break

    else:
        # Erreur de saisie
        print("Saisie incorrecte.")

EXERCICE TEMPÉRATURE

def convertir_temperature(temperature, unit_depart, unit_arrivee): #fonction qui convertir la température

    Arguments:
        temperature: La température à convertir.
        unit_depart: L'unité de départ ('Celsius' ou 'Fahrenheit').
        unit_arrivee: L'unité d'arrivée ('Celsius' ou 'Fahrenheit').

    Returns:
        La température convertie.
    """

    #Si l'unité de départ est celsius et l'unité d'arrivée est Fahrenheit alors température température Farheneit correpond à température Celsius *1,8+32     
    if unit_depart == "Celsius" and unit_arrivee == "Fahrenheit": 
        return temperature * 1.8 + 32
    elif unit_depart == "Fahrenheit" and unit_arrivee == "Celsius":
        return (temperature - 32) / 1.8
    else:
        raise ValueError("Unité de départ ou d'arrivée invalide.")

print(convertir_temperature(20, "Celsius", "Fahrenheit"))
68.0
print(convertir_temperature(50, "Celsius", "Fahrenheit"))
122.0


EXERCICE CALCUL IMC 
def calculer_imc(poids, taille):
    """Calcule l'Indice de Masse Corporelle (IMC).

    Args:
        poids: Le poids en kilogrammes.
        taille: La taille en mètres.

    Returns:
        L'IMC.
    """

    return poids / taille ** 2
    
    print(calculer_imc(77, 1.76))
24.857954545454547
