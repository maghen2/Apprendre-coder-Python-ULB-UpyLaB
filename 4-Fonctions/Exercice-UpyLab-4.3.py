# Exercice UpyLab 4.3 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction booléenne premier(n) qui reçoit un nombre entier positif n et qui renvoie True si n est un nombre premier, et False sinon.
# Ensuite, écrire un programme qui lit une valeur entière x et affiche, grâce à des appels à la fonction premier, tous les nombres premiers strictement inférieurs à x, chacun sur sa propre ligne.

def premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1): # vérifie si n est divisible par un nombre entre 2 et la racine carrée de n
        if n % i == 0:
            return False
    return True

x = int(input())
for num in range(2, x):
    if premier(num):
        print(num)
