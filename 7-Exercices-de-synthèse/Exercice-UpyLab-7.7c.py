# Exercice UpyLab 7.7c - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction check_regions qui prend en paramètre une grille sous forme de matrice à deux dimensions et vérifie si toutes les régions sont valides (c’est-à-dire que dans chaque région, chaque chiffre apparaît une et une seule fois).

# Exemple 1
# L’appel de la fonction suivant :

# check_regions([[9, 6, 3, 1, 7, 4, 2, 5, 8],
#               [1, 7, 8, 3, 2, 5, 6, 4, 9],
#               [2, 5, 4, 6, 8, 9, 7, 3, 1],
#               [8, 2, 1, 4, 3, 7, 5, 9, 6],
#               [4, 9, 6, 8, 5, 2, 3, 1, 7],
#               [7, 3, 5, 9, 6, 1, 8, 2, 4],
#               [5, 8, 9, 7, 1, 3, 4, 6, 2],
#               [3, 1, 7, 2, 4, 6, 9, 8, 5],
#               [6, 4, 2, 5, 9, 8, 1, 7, 3]])
# retourne :

# True

def check_regions(grid):
    for i in range(0, len(grid), 3):
        for j in range(0, len(grid[0]), 3):
            region = [grid[row][col] for row in range(i, i+3) for col in range(j, j+3)]
            if len(set(region)) != len(region):
                return False
    return True
    
#Test
print(check_regions([[9, 6, 3, 1, 7, 4, 2, 5, 8],
              [1, 7, 8, 3, 2, 5, 6, 4, 9],
              [2, 5, 4, 6, 8, 9, 7, 3, 1],
              [8, 2, 1, 4, 3, 7, 5, 9, 6],
              [4, 9, 6, 8, 5, 2, 3, 1, 7],
              [7, 3, 5, 9, 6, 1, 8, 2, 4],
              [5, 8, 9, 7, 1, 3, 4, 6, 2],
              [3, 1, 7, 2, 4, 6, 9, 8, 5],
              [6, 4, 2, 5, 9, 8, 1, 7, 3]]))