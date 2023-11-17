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
n = int(input("Entrez un nombre entier N : "))

# Initialise la somme à 0
somme = 0

# Boucle sur les nombres de 1 à N
for i in range(1, n + 1):
    # Ajoute le nombre courant à la somme
    somme += i

# Affiche la somme
print("La somme des nombres de 1 à N est", somme)

# Demande à l'utilisateur un nombre entier N
n = int(input("Entrez un nombre entier N : "))

# Initialise la somme à 0
somme = 0

# Boucle sur les nombres de 1 à N
for i in range(1, n + 1):
    # Ajoute le nombre courant à la somme
    somme += i

# Affiche la somme
print("La somme des nombres de 1 à N est", somme)

Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
n=int(input("Choisissez un nombre entier N:"))
Choisissez un nombre entier N:5
somme=0
for i in range (1,n+1):
    somme +=i

    
print("La somme des nombre de 1 à N correspond à",somme)
La somme des nombre de 1 à N correspond à 15
