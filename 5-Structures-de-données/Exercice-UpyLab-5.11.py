# Exercice UpyLab 5.11 - Parcours : bleu rouge
 
# Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction intersection(v, w) qui calcule l’intersection entre deux chaînes de caractères v et w.

# On définit l’intersection de deux mots comme étant la plus grande partie commune à ces deux mots. Par exemple, l’intersection de « programme » et « grammaire » est « gramm ».

# Si les deux chaînes n’ont aucun caractère en commun, la fonction retourne la chaîne vide, ''.

# Si plusieurs solutions sont possibles, la fonction retournera la sous-chaîne d’indice minimal dans v. Par exemple, intersection('bbaacc', 'aabb') renvoie 'bb'.
def intersection(v, w):
    common_part = ''
    for i in range(len(v)):
        for j in range(i+1, len(v)+1):
            if v[i:j] in w and len(v[i:j]) > len(common_part):
                common_part = v[i:j]
    return common_part


print(intersection('programme', 'grammaire')) 