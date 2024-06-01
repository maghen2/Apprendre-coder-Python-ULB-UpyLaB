# Exercice UpyLab 5.10 - Parcours : vert bleu rouge
 
# Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction dupliques qui reçoit une séquence en paramètre.

# La fonction doit renvoyer la valeur booléenne True si la séquence passée en paramètre contient des éléments dupliqués, et la valeur booléenne False sinon.
def dupliques(sequence):
    return len(sequence) != len(set(sequence)) # on compare la longueur de la séquence avec la longueur de la séquence transformée en ensemble car les ensembles n'admettent pas de doublon
