# Exercice UpyLab 5.7 - Parcours : vert bleu rouge
 
# Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction plus_grand_bord(w) qui reçoit un mot w et retourne le plus grand bord de ce mot.

# On dit qu’un mot u est un bord du mot w si u est à la fois un préfixe strict et un suffixe strict de w, c’est-à-dire qu’on retrouve le mot u au début et à la fin du mot w, sans que u soit égal à w lui-même.

# Exemples : 'a' et 'abda' sont des bords de 'abdabda'. En effet, 'abdabda' commence et se termine par 'a', ainsi que par 'abda'. Le plus grand bord de 'abdabda' est 'abda'.

# Si w n’a pas de bord, la fonction retourne la chaîne de caractères vide.

def plus_grand_bord(w):
    n = len(w)
    for i in range(n//2):
        if w[:i] == w[n-i:]: # comparaison à partir du milieu vers les expremités du mot afin de retourner le plus grand bord possible
            return w[:i]
    return ""
