Exercice UpyLab 5.13 - Parcours : rouge
 
Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier
L’exercice est le même que le précédent, mais ici, si les paramètres ont le type attendu, la fonction modifie la liste en place et ne retourne rien. Si les paramètres ne sont pas valides, une erreur se produit à l’exécution.

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