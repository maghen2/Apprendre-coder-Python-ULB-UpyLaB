# Exercice UpyLab 5.9 - Parcours : vert bleu rouge
 
# Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Une anagramme d’un mot v est un mot w qui comprend les mêmes lettres que le mot initial v, en même quantité, mais non nécessairement dans le même ordre (par exemple, « marion » et « romina » sont des anagrammes). Notez que anagramme est un mot féminin.

# Écrire une fonction anagrammes(v, w) qui renvoie la valeur booléenne True si les mots v et w sont des anagrammes.

# La fonction retourne la valeur booléenne False dans le cas contraire.
def anagrammes(v, w):
    return sorted(v) == sorted(w) # on compare les deux mots triés
