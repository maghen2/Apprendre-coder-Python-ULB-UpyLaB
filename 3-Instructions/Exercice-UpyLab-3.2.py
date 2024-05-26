# Exercice UpyLab 3.2 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier

# Écrire un programme qui, si temperature (entier lu sur input correspondant à la température maximale prévue pour aujourd’hui) est strictement supérieur à 0, teste si temperature est inférieur ou égal à 10, auquel cas il imprime le texte :

# Il va faire frais.

# et qui, si temperature n’est pas supérieur à 0, imprime le texte :

# Il va faire froid.

# Dans les autres cas, le programme n’imprime rien.
temperature = int(input())

if temperature > 0:
    if temperature <= 10:
        print("Il va faire frais.")
else:
    print("Il va faire froid.")
