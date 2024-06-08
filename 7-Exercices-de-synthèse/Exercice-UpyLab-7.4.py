# Exercice UpyLab 7.4 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier, Jacky Trinh
# Puissance 4 est un jeu de stratégie combinatoire abstrait dont le but est d’aligner une suite de quatre pions de même couleur sur une grille comptant six rangées et sept colonnes.

# Chaque joueur possède vingt-et-un pions d’une couleur (jaune ou rouge). À chaque tour, le joueur suivant doit placer un pion dans la colonne de son choix. Le pion tombe dans la position la plus basse possible.

# Le vainqueur est le premier qui a réussi à aligner horizontalement, verticalement ou diagonalement, de manière consécutive, quatre de ses pions.

# Écrire une fonction placer_pion(couleur, colonne, grille) où :

# couleur est la couleur du pion, qui peut être soit 'R' (rouge), soit 'J' (jaune),

# colonne est l’indice de la colonne où le joueur souhaite placer le pion (allant de 0 à 6),

# grille est la grille de jeu sous forme de matrice.

# Cette matrice contient donc six listes de lignes contenant chacune sept éléments.

# La ligne à l’indice 0 représente le bas du jeu.

# Les éléments de cette matrice seront soit 'R', soit 'J' ou soit 'V' pour un emplacement encore vide.

# Cette fonction placera un pion dans la grille du jeu et renverra un couple de valeurs :

# si le placement est possible, la valeur booléenne True et la grille modifiée,

# sinon, la valeur booléenne False et la grille non modifiée.

# Exemple 1
# L’appel suivant de la fonction :

# placer_pion("R", 3, [['V', 'V', 'V', 'J', 'V', 'V', 'V'],
#                      ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#                      ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#                      ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#                      ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#                      ['V', 'V', 'V', 'V', 'V', 'V', 'V']])
# doit retourner :

# (True, [['V', 'V', 'V', 'J', 'V', 'V', 'V'],
#         ['V', 'V', 'V', 'R', 'V', 'V', 'V'],
#         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#         ['V', 'V', 'V', 'V', 'V', 'V', 'V']])
# Exemple 2
# L’appel suivant de la fonction :

# placer_pion("J", 4, [['J', 'J', 'J', 'J', 'R', 'R', 'R'],
#                      ['R', 'R', 'R', 'R', 'R', 'V', 'V'],
#                      ['J', 'J', 'J', 'J', 'J', 'V', 'V'],
#                      ['V', 'R', 'J', 'R', 'J', 'V', 'V'],
#                      ['V', 'V', 'V', 'V', 'J', 'V', 'V'],
#                      ['V', 'V', 'V', 'V', 'R', 'V', 'V']])
# doit retourner :

# (False, [['J', 'J', 'J', 'J', 'R', 'R', 'R'],
#          ['R', 'R', 'R', 'R', 'R', 'V', 'V'],
#          ['J', 'J', 'J', 'J', 'J', 'V', 'V'],
#          ['V', 'R', 'J', 'R', 'J', 'V', 'V'],
#          ['V', 'V', 'V', 'V', 'J', 'V', 'V'],
#          ['V', 'V', 'V', 'V', 'R', 'V', 'V']])
# Consignes
# Dans cet exercice, il vous est demandé d’écrire seulement la fonction placer_pion. Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

# Vous pourrez supposer que les arguments passés à la fonction seront valides.

# Il n’est pas demandé de vérifier si la grille contient un alignement gagnant.

def placer_pion(couleur, colonne, grille):
    if colonne < 0 or colonne >= len(grille[0]):
        return False, grille
    
    for i in range(len(grille)-1, -1, -1):
        if grille[i][colonne] == 'V':
            grille[i][colonne] = couleur
            return True, grille
    
    return False, grille