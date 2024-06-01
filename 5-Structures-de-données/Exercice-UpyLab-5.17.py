# Exercice UpyLab 5.17 - Parcours : bleu rouge
# Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Cet exercice peut aussi se résoudre sans utiliser la technique de compréhension de liste. Mais les solutions sont beaucoup plus courtes avec cette technique ! Nous vous demandons donc si possible de les réaliser avec du code utilisant des compréhensions de liste.

 

# On considère une liste qui décrit une séquence t. Chaque élément de cette liste est un tuple de deux composantes : le nombre de répétitions successives de l’élément x dans la séquence t, et l’élément x lui-même.

# Par exemple, la liste [(1, 'He'), (2, 'l'), (1,'o')] décrit la séquence "Hello".

# Écrire une fonction decompresse qui reçoit une telle liste en paramètre et renvoie la séquence t sous forme d’une nouvelle liste.

# Exemple
# L’appel suivant de la fonction :

# decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')])
# doit retourner :

# [1, 1, 1, 1, 'test', 'test', 3, 3, 3, 'bonjour']

def decompresse(lst):
    result = []
    for (count, element) in lst:
        result.extend([element] * count)
    return result

print(decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')]))