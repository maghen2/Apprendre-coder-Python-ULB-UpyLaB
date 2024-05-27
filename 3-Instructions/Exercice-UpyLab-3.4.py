# Exercice UpyLab 3.4 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire un programme qui teste la parité d’un nombre entier lu sur input et imprime True si le nombre est pair, False dans le cas contraire.
number = int(input())
if number % 2 == 0:
    print(True)
else:
    print(False)