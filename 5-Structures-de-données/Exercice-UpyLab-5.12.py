# Exercice UpyLab 5.12 - Parcours : bleu rouge
 
# Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction my_insert qui reçoit comme premier paramètre une liste d’entiers relatifs triée par ordre croissant et comme deuxième paramètre un entier relatif n, et qui renvoie une liste correspondant à la liste reçue, mais dans laquelle le nombre n a été inséré à la bonne place.

# La liste donnée en paramètre ne doit pas être modifiée par votre fonction.

# Vous pouvez supposer que le premier paramètre sera bien une liste triée d’entiers, mais si le deuxième paramètre n’est pas du bon type, la fonction retourne None.
def my_insert(lst, n):
    if not isinstance(n, int):
        return None
    
    new_lst = lst.copy()
    new_lst.append(n)
    new_lst.sort()
    
    return new_lst
print(my_insert([1, 3, 5], 4))
print(my_insert([2, 3, 5], 1))
print(my_insert([2, 3, 5], 0.5))