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

