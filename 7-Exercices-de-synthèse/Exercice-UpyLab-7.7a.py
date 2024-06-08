# Énoncé:
# Source MOOC « Apprendre à coder avec Python » - Session 4

# Le sudoku est un jeu de logique dans lequel le joueur reçoit une grille de 9 x 9 cases, chacune pouvant contenir un chiffre de 1 à 9 ou bien être vide. La grille est divisée en 9 lignes, 9 colonnes ainsi qu’en 9 « sous-grilles », appelées régions, formées de 3 x 3 boîtes contiguës. Le but du jeu est de remplir les cases vides avec des chiffres de 1 à 9, de telle sorte que, dans chaque ligne, chaque colonne et chaque région, soient présents tous les chiffres de 1 à 9, sans doublons.

# Le but de cet exercice est d'écrire une fonction qui indiquera si la grille passée en argument est une grille de sudoku correctement remplie.
# Pour cela, vous allez écrire trois fonctions annexes que vous pourrez tester et valider dans des exercices intermédiaires 6.17a à 6.17c.

# Exercice UpyLab 7.7a - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction check_rows(grid) qui prend en paramètre une grille sous forme de matrice à deux dimensions et vérifie si toutes les lignes sont valides (c’est-à-dire que sur chaque ligne, chaque chiffre apparaît une et une seule fois).

# Exemple 1
# L’appel de la fonction suivant :

# check_rows([[9, 6, 3, 1, 7, 4, 2, 5, 8],
#             [1, 7, 8, 3, 2, 5, 6, 4, 9],
#             [2, 5, 4, 6, 8, 9, 7, 3, 1],
#             [8, 2, 1, 4, 3, 7, 5, 9, 6],
#             [4, 9, 6, 8, 5, 2, 3, 1, 7],
#             [7, 3, 5, 9, 6, 1, 8, 2, 4],
#             [5, 8, 9, 7, 1, 3, 4, 6, 2],
#             [3, 1, 7, 2, 4, 6, 9, 8, 5],
#             [6, 4, 2, 5, 9, 8, 1, 7, 3]])
# retourne :

# True
def check_rows(grid):
    for row in grid:
        if len(set(row)) != len(row):
            return False
    return True

# Test
print(check_rows([[9, 6, 3, 1, 7, 4, 2, 5, 8],
            [1, 7, 8, 3, 2, 5, 6, 4, 9],
            [2, 5, 4, 6, 8, 9, 7, 3, 1],
            [8, 2, 1, 4, 3, 7, 5, 9, 6],
            [4, 9, 6, 8, 5, 2, 3, 1, 7],
            [7, 3, 5, 9, 6, 1, 8, 2, 4],
            [5, 8, 9, 7, 1, 3, 4, 6, 2],
            [3, 1, 7, 2, 4, 6, 9, 8, 5],
            [6, 4, 2, 5, 9, 8, 1, 7, 3]])) # True
