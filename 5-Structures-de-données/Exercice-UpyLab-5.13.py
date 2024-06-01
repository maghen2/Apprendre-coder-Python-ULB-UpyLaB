# Exercice UpyLab 5.13 - Parcours : rouge
 
# Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# L’exercice est le même que le précédent, mais ici, si les paramètres ont le type attendu, la fonction modifie la liste en place et ne retourne rien. Si les paramètres ne sont pas valides, une erreur se produit à l’exécution.

def my_insert(lst, n):
    assert isinstance(n, int) #, "AssertionError"
    lst.append(n)
    lst.sort()

lst = [1, 3, 5]
my_insert(lst, 4)
print(lst)

my_insert(lst, 4.5)
print(lst)