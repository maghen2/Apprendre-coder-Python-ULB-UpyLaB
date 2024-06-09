# Exercice UpyLab 7.8 - Parcours : rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Le sudoku est un jeu de logique dans lequel le joueur reçoit une grille de 9 x 9 cases, chacune pouvant contenir un chiffre de 1 à 9 ou bien être vide. La grille est divisée en 9 lignes, 9 colonnes ainsi qu’en 9 « sous-grilles », appelées régions, formées de 3 x 3 boîtes contiguës. Le but du jeu est de remplir les cases vides avec des chiffres de 1 à 9, de telle sorte que, dans chaque ligne, chaque colonne et chaque région, soient présents tous les chiffres de 1 à 9, sans doublons.

# Une méthode de résolution passe par l’analyse des candidats uniques. Ce qu’on appelle candidat est un nombre permis pour une case car on ne le retrouve pas ailleurs dans la ligne, la colonne et la région de cette case.

# Si une grille est telle que chaque case vide se retrouve avec un candidat unique, alors la résolution du sudoku est évidente.

# Des deux grilles suivantes, seule la première peut être résolue de cette manière : par exemple, en indiçant le tableau à partir de 0, (0,0) étant en haut à gauche, à la case d’indice (4,7), seule la valeur 3 est possible. On peut ensuite faire de même jusqu’à la résolution complète du sudoku.

# https://upylab.ulb.ac.be/pub/static/exemples_grilles.png
# Écrire une fonction naked_single(grid) qui reçoit en paramètre une matrice 9 x 9 d’entiers représentant une grille de sudoku, et qui renvoie un couple de valeurs :

# un booléen ok qui indique si la grille peut être résolue en utilisant cette seule méthode du candidat unique,

# la grille complétée si ok est égal à True, None sinon.

# Exemple 1
# L’appel de la fonction suivant :

# naked_single([[4, 0, 3, 0, 9, 6, 0, 1, 0],
#               [0, 0, 2, 8, 0, 1, 0, 0, 3],
#               [0, 1, 0, 0, 0, 0, 0, 0, 7],
#               [0, 4, 0, 7, 0, 0, 0, 2, 6],
#               [5, 0, 7, 0, 1, 0, 4, 0, 9],
#               [1, 2, 0, 0, 0, 3, 0, 8, 0],
#               [2, 0, 0, 0, 0, 0, 0, 7, 0],
#               [7, 0, 0, 2, 0, 9, 8, 0, 0],
#               [0, 6, 0, 1, 5, 0, 3, 0, 2]])
# retourne :

# (True, [[4, 7, 3, 5, 9, 6, 2, 1, 8],
#         [6, 5, 2, 8, 7, 1, 9, 4, 3],
#         [9, 1, 8, 3, 2, 4, 5, 6, 7],
#         [3, 4, 9, 7, 8, 5, 1, 2, 6],
#         [5, 8, 7, 6, 1, 2, 4, 3, 9],
#         [1, 2, 6, 9, 4, 3, 7, 8, 5],
#         [2, 9, 5, 4, 3, 8, 6, 7, 1],
#         [7, 3, 1, 2, 6, 9, 8, 5, 4],
#         [8, 6, 4, 1, 5, 7, 3, 9, 2]])
# Exemple 2
# L’appel de la fonction suivant :

# naked_single([[0, 0, 6, 0, 4, 0, 1, 0, 0],
#               [0, 5, 0, 0, 9, 0, 0, 6, 0],
#               [8, 0, 0, 0, 0, 0, 0, 0, 5],
#               [0, 0, 0, 3, 0, 4, 0, 0, 0],
#               [3, 1, 0, 0, 0, 0, 0, 4, 8],
#               [0, 0, 0, 8, 0, 7, 0, 0, 0],
#               [6, 0, 0, 0, 0, 0, 0, 0, 9],
#               [0, 2, 0, 0, 3, 0, 0, 5, 0],
#               [0, 0, 1, 0, 5, 0, 7, 0, 0]])
# retourne :

# (False, None)
# Consignes
# Dans la grille passée en paramètre, les cases vides sont représentées par l’entier 0.

def check_rows(grid):
    for row in grid:
        if len(set(row)) != len(row):
            return False
    return True

def check_cols(grid):
    for col in range(len(grid[0])):
        column = [grid[row][col] for row in range(len(grid))]
        if len(set(column)) != len(column):
            return False
    return True

def check_regions(grid):
    for i in range(0, len(grid), 3):
        for j in range(0, len(grid[0]), 3):
            region = [grid[row][col] for row in range(i, i+3) for col in range(j, j+3)]
            if len(set(region)) != len(region):
                return False
    return True

def check_sudoku(grid):
    if check_rows(grid) and check_cols(grid) and check_regions(grid):
        return True
    else:
        return False
    
    # Fonction auxiliaire pour extraire la région d'une case donnée
def get_region(grid, i, j):
  region_i = i // 3
  region_j = j // 3
  region = [grid[row][col] for row in range(region_i * 3, region_i * 3 + 3) for col in range(region_j * 3, region_j * 3 + 3)]
  return region

 #   Fonction qui vérifie si un sudoku peut être résolu par la méthode du candidat unique et retourne la grille complétée si possible.   
def naked_single(grid):
 
 # On crée une copie de la grille pour ne pas modifier la grille d'origine.
  grid_copy = [[n for n in ligne] for ligne in grid]

  # On parcourt la grille.
  for i in range(9):
    for j in range(9):
      # Si la case est vide (représentée par 0), on cherche les candidats possibles.
      if grid_copy[i][j] == 0:
        possibles = set(range(1, 10))  # Ensemble des candidats possibles.

        # On supprime les candidats déjà présents dans la ligne, la colonne et la région.
        if not (check_rows(grid_copy[i:]) and check_cols([ligne[j] for ligne in grid_copy]) and check_regions(get_region(grid_copy, i, j))):
          return False, None  # Sudoku invalide, on arrête

        for k in range(9):
          if grid_copy[i][k] != 0:
            possibles.remove(grid_copy[i][k])
          if grid_copy[k][j] != 0:
            possibles.remove(grid_copy[k][j])

        # S'il n'y a qu'un seul candidat possible, on le place dans la grille et on retourne True.
        if len(possibles) == 1:
          grid_copy[i][j] = list(possibles)[0]
          return True, grid_copy

  # Si aucun candidat unique n'a été trouvé, on retourne False et None.
  return False, None



# Test
print(naked_single([[4, 0, 3, 0, 9, 6, 0, 1, 0],
              [0, 0, 2, 8, 0, 1, 0, 0, 3],
              [0, 1, 0, 0, 0, 0, 0, 0, 7],
              [0, 4, 0, 7, 0, 0, 0, 2, 6],
              [5, 0, 7, 0, 1, 0, 4, 0, 9],
              [1, 2, 0, 0, 0, 3, 0, 8, 0],
              [2, 0, 0, 0, 0, 0, 0, 7, 0],
              [7, 0, 0, 2, 0, 9, 8, 0, 0],
              [0, 6, 0, 1, 5, 0, 3, 0, 2]]))

