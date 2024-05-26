# Exercice UpyLaB 3.1 - Parcours vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire un programme qui lit 3 nombres entiers, et qui, si au moins deux d’entre eux ont la même valeur, imprime cette valeur (le programme n’imprime rien dans le cas contraire).

# Read three integers
num1 = int(input())
num2 = int(input())
num3 = int(input())

# Check if at least two numbers are equal
if num1 == num2 or num1 == num3 :
    print(num1)
elif num2 == num3 :
    print(num2)
 