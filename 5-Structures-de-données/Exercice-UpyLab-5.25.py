# Exercice UpyLab 5.25 - Parcours : bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction trace(M) qui reçoit en paramètre une matrice M de taille {n}\times{n} contenant des valeurs numériques (de type int ou float), et qui renvoie sa trace, c’est-à-dire la somme de tous les éléments de la première diagonale.

# Exemple 1
# L’appel suivant de la fonction :

# trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# doit retourner :

# 15
# En effet, 1 + 5 + 9 est égal à 15.

# Exemple 2
# L’appel suivant de la fonction :

# trace([])
# doit retourner :
def trace(M):
    if len(M) == 0:
        return 0
    else:
        n = len(M)
        trace_sum = 0
        for i in range(n):
            trace_sum += M[i][i]
        return trace_sum
    
print(trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))