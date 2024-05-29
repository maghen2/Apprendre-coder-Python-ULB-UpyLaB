# Exercice UpyLab 3.13 - Parcours : bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire un programme qui additionne des valeurs naturelles lues sur entrée et affiche le résultat.
# La première donnée lue ne fait pas partie des valeurs à sommer. Elle détermine si la liste contient un nombre déterminé à l’avance de valeurs à lire ou non :

# si cette valeur est un nombre positif ou nul, elle donne le nombre de valeurs à lire et à sommer ;

# si elle est égale à -1, cela signifie qu’elle est suivie d’une liste de données à lire qui sera terminée par le caractère "F" signifiant que la liste est terminée.
total = count = 0
num_values = int(input()) # Read the number of values to sum

if num_values >= 0:
    for count in range(num_values):
        value = int(input()) # Read a value
        total += value
        count += 1

elif num_values == -1:
    while True:
        value = input() # Read a value (or "F" to finish)
        if value == "F":
            break
        total += int(value)

print(total)