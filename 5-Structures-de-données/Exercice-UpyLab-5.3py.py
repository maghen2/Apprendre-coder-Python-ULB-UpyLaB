# Exercice UpyLab 5.3 - Parcours : vert bleu rouge
# Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction duree qui reçoit deux paramètres debut et fin. Ces derniers sont des couples (tuples de deux composantes) dont la première composante représente une heure et la seconde les minutes.

# Cette fonction doit calculer la durée qui s’est écoulée entre ces deux instants. Le résultat sera donné sous la forme d’un tuple (heure, minutes).

def duree(debut, fin):
    duree[0] = fin[0] - debut[0] 
    duree[1] = fin[1] - debut[1] 
    if duree[1] < 0 :
        duree[1] +=60
        duree[0] -=1
    return duree
