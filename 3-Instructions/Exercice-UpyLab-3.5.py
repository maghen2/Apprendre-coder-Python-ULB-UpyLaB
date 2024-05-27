# Exercice UpyLab 3.5 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier

# Écrire un programme qui lit en entrée deux nombres entiers strictement positifs, et qui vérifie qu’aucun des deux n’est un diviseur de l’autre.

# Si tel est bien le cas, le programme imprime True. Sinon, il imprime False.

num1 = int(input())
num2 = int(input())

if(num1>0 and num2>0):
    if num1 % num2 != 0 and num2 % num1 != 0:
        print(True)
    else:
        print(False)