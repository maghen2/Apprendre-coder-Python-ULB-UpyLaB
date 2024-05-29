# Exercice UpyLaB 4.1 - Parcours vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
 
# Écrire une fonction deux_egaux(a, b, c) qui reçoit trois nombres en paramètre et qui renvoie la valeur booléenne True si au moins deux de ces nombres ont la même valeur, et la valeur booléenne False sinon.

# Ensuite, écrire un programme qui lit trois données de type int, x, y et z, et affiche le résultat de l’exécution de deux_egaux(x, y, z).
def deux_egaux(a, b, c):
    if a == b or a == c or b == c:
        return True
    else:
        return False

a = int(input())
b = int(input())
c = int(input())

result = deux_egaux(a, b, c)
print(result)