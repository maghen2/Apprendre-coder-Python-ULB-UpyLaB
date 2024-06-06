# Exercice UpyLab 5.24 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction print_mat(M) qui reçoit une matrice M en paramètre et affiche son contenu.

# Les éléments d’une même ligne de la matrice seront affichés sur une même ligne, et séparés par une espace, les éléments de la ligne suivante étant affichés sur une nouvelle ligne.

# Exemple
# L’appel suivant de la fonction :

# print_mat([[1, 2], [3, 4], [5, 6]])
# doit afficher :

# 1 2
# 3 4
# 5 6

#print_mat([['H', 'E', 'L', 'L', 'O'], ['W', 'O', 'R', 'L', 'D']])
# doit afficher :
# H E L L O
# W O R L D
def print_mat(M):
    for row in M:
        print(' '.join(map(str, row)))

print_mat([[1, 2], [3, 4], [5, 6]])
print_mat([['H', 'E', 'L', 'L', 'O'], ['W', 'O', 'R', 'L', 'D']])