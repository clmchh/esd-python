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
    # Initialise la position du début et de la fin du mot
    debut = 0
    fin = len(mot) - 1

    # Tant que le début et la fin ne se sont pas rencontrés
    while debut < fin:
        # Si les caractères ne sont pas les mêmes
        if mot[debut] != mot[fin]:
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
