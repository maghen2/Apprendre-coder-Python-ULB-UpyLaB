# Exercice UpyLab 3.3 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire un programme qui lit trois entiers a, b et c en input. Ensuite :

# si l’entier c est égal à 1, alors le programme affiche la valeur de a + b ;

# si c vaut 2, alors le programme affiche la valeur de a - b ;

# si c est égal à 3, alors l’output sera la valeur de a.b (produit de a par b) ;

# enfin, si la valeur 4 est assignée à la variable c, alors le programme affiche la valeur de a^2 + a.b ;

# et si c contient une autre valeur, le programme affiche le message Erreur.
a = int(input())
b = int(input())
c = int(input())

if c == 1:
    result = a + b
elif c == 2:
    result = a - b
elif c == 3:
    result = a * b
elif c == 4:
    result = a**2 + a * b
else:
    result = "Erreur"

print(result)