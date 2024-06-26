# Exercice UpyLab 3.12 - Parcours : bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Cet exercice propose une variante de l’exercice précédent sur le carré de X.

# Écrire un programme qui lit en entrée une valeur naturelle n et qui affiche à l’écran un triangle supérieur droit formé de X (voir exemples plus bas).
# Exemple 1
# Avec la donnée lue suivante :

# 6
# le résultat à imprimer vaudra :

# XXXXXX
#  XXXXX
#   XXXX
#    XXX
#     XX
#      X

n = int(input()) # Read the size of the triangle (number of lines)

for i in range(n):
    print(" " * i + "X" * (n - i))