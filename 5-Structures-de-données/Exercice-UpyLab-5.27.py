# Exercice UpyLab 5.27 - Parcours : rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction symetrie_horizontale(A) qui reçoit une matrice carrée A (de taille {n}\times{n}) et qui renvoie l’image de A par symétrie horizontale par rapport à la ligne du milieu : la première ligne devenant la dernière, la seconde, l’avant-dernière, etc.

# Exemple 1
# L’appel suivant de la fonction :

# symetrie_horizontale([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# doit retourner :

# [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
# Exemple 2
# L’appel suivant de la fonction :

# symetrie_horizontale([['a', 'b'], ['c', 'd']])
# doit retourner :

# [['c', 'd'], ['a', 'b']]
# Exemple 3
# L’appel suivant de la fonction :

# symetrie_horizontale([])
# doit retourner :

# []

def symetrie_horizontale(A):
    return A[::-1]

print(symetrie_horizontale([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(symetrie_horizontale([['a', 'b'], ['c', 'd']]))
print(symetrie_horizontale([]))