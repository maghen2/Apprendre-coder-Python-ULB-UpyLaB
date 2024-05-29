# Exercice UpyLab 3.10 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire un programme qui calcule la taille moyenne (en nombre de salariés) des Petites et Moyennes Entreprises de la région.
# Les tailles seront données en entrée, chacune sur sa propre ligne, et la fin des données sera signalée par la valeur sentinelle -1. Cette valeur n’est pas à comptabiliser pour le calcul de la moyenne, mais indique que l’ensemble des valeurs a été donné.

# Après l’entrée de cette valeur sentinelle -1, le programme affiche la valeur de la moyenne arithmétique calculée.

# On suppose que la suite des tailles contient toujours au moins un élément avant la valeur sentinelle -1, et que toutes ces valeurs sont positives ou nulles.
total = 0
count = 0

while True:
    size = int(input()) # Read the size of a company 
    if size == -1:
        break
    total += size
    count += 1

average = total / count
print(average)
