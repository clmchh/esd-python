Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
a=51
while (a>0):
    a=a-1
    print(a)

    
50
49
48
47
46
45
44
43
42
41
40
39
38
37
36
35
34
33
32
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
a=50
while a>=0:
    print(a)
    a-=1

    
50
49
48
47
46
45
44
43
42
41
40
39
38
37
36
35
34
33
32
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
a=0
while a<=50
SyntaxError: incomplete input
a=0
while a<=50:
    if a%3==0:
        print(a)
    a+=1

    
0
3
6
9
12
15
18
21
24
27
30
33
36
39
42
45
48
for i in range(1,21):
    resultat=7*i
    print(f"7x{i}={résultat}")

    
Traceback (most recent call last):
  File "<pyshell#21>", line 3, in <module>
    print(f"7x{i}={résultat}")
NameError: name 'résultat' is not defined. Did you mean: 'resultat'?
yes
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    yes
NameError: name 'yes' is not defined



for i in range(1,21):
    resultat=7*i
    print(f"7xi}={resultat}")
    
SyntaxError: f-string: single '}' is not allowed
for i in range (1,21):
    resultat=7*i
    print(f"7x{i}={resultat}")

    
7x1=7
7x2=14
7x3=21
7x4=28
7x5=35
7x6=42
7x7=49
7x8=56
7x9=63
7x10=70
7x11=77
7x12=84
7x13=91
7x14=98
7x15=105
7x16=112
7x17=119
7x18=126
7x19=133
7x20=140

euro=1
conversion_rate=1.65
while euros<=16384:
    print(f"{euros} euro(s) = {euros * conversion_rate:.2f} dollar(s)")
    euros*=2

    
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    while euros<=16384:
NameError: name 'euros' is not defined. Did you mean: 'euro'?
euros = 1
conversion_rate = 1.65

while euros <= 16384:
    print(f"{euros} euro(s) = {euros * conversion_rate:.2f} dollar(s)")
    euros *= 2  # Double la somme d'euros à chaque itération

SyntaxError: multiple statements found while compiling a single statement

euros = 1
conversion_rate = 1.65

... while euros <= 16384:
...     print(f"{euros} euro(s) = {euros * conversion_rate:.2f} dollar(s)")
...     euros *= 2
...     
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> # Initialise le premier terme de la suite
... terme = 1
... 
... # Affiche le premier terme
... print(f"Terme 1: {terme}")
... 
... # Calcule et affiche les 11 termes suivants
... for i in range(2, 13):
...     terme *= 3  # Multiplie le terme précédent par 3 pour obtenir le terme suivant
...     print(f"Terme {i}: {terme}")
... 
SyntaxError: multiple statements found while compiling a single statement
>>> 
...  
>>> terme=1
>>> print(f"terme1:{terme}")
terme1:1
>>> for i in range(2,13):
...     terme*=3
...     print(f"terme{i}: {terme}")
... 
...     
terme2: 3
terme3: 9
terme4: 27
terme5: 81
terme6: 243
terme7: 729
terme8: 2187
terme9: 6561
terme10: 19683
terme11: 59049
terme12: 177147
