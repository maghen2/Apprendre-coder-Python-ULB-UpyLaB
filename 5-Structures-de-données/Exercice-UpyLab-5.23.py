# Exercice UpyLab 5.23 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction init_mat(m, n) qui construit et renvoie une matrice d’entiers initialisée à la matrice nulle et de dimension m x n.

# Exemple 1
# L’appel suivant de la fonction :

# init_mat(2, 3)
# doit retourner :

# [[0, 0, 0], [0, 0, 0]]
# Exemple 2
# L’appel suivant de la fonction :

# init_mat(0, 0)
# doit retourner :

# []

def init_mat(m, n):
    return [[0] * n for _ in range(m)]
