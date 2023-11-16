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
