# Exercice UpyLab 7.3 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Voici le début d’une suite logique inventée par John Horton Conway (et connue donc sous le nom de suite de Conway).

# 1
# 1 1
# 2 1
# 1 2 1 1
# 1 1 1 2 2 1
# 3 1 2 2 1 1
# ...
# Chaque ligne, à partir de la deuxième, décrit la précédente :

# la première ligne, 1, est formée de un “1”, d’où la deuxième ligne : 1 1 ;

# la troisième ligne décrit la deuxième ligne, où l’on voit deux “1”, d’où 2 1 ;

# la quatrième ligne décrit la troisième ligne, où l’on voit un “2” et un “1”, d’où 1 2 1 1 ;

# et ainsi de suite.

# Écrire une fonction next_line(line) qui reçoit une liste d’entiers, et qui retourne la liste correspondant à la ligne suivante.

# Notez que les valeurs de la liste reçue sont toujours entières, mais cette dernière peut ne pas correspondre à une suite de Conway (par exemple [4,2] pourrait être donné).
# Exemple 1
# L’appel suivant de la fonction :

# next_line([1, 2, 1, 1])
# doit retourner :

# [1, 1, 1, 2, 2, 1]
# Exemple 2
# L’appel suivant de la fonction :

# next_line([1])
# doit retourner :

# [1, 1]
# Exemple 3
# L’appel suivant de la fonction :

# next_line([])
# doit retourner :

# [1]
 
# Consignes
# Dans cet exercice, il vous est demandé d’écrire seulement la fonction next_line. Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

# Notez que l’appel next_line([]) sur la liste vide retourne par convention la liste [1].

# AIDE EN CAS DE BESOIN
# Conseils
# Il n’est demandé ici que de définir la fonction. Mais pour tester son fonctionnement dans votre IDE, pensez à ajouter du code qui l’appelle et teste son résultat, sur plusieurs valeurs, comme print(next_line([1, 2,1, 1])) par exemple.

# N’hésitez pas à tester votre fonction sur les cas « limites » comme la liste vide, [], ou la liste singleton [1], en vous référant aux exemples donnés.

