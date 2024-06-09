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
