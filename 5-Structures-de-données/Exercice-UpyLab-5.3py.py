# Exercice UpyLab 5.3 - Parcours : vert bleu rouge
# Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction duree qui reçoit deux paramètres debut et fin. Ces derniers sont des couples (tuples de deux composantes) dont la première composante représente une heure et la seconde les minutes.

# Cette fonction doit calculer la durée qui s’est écoulée entre ces deux instants. Le résultat sera donné sous la forme d’un tuple (heure, minutes).

def duree(debut, fin):
    periode = (fin[0] - debut[0], fin[1] - debut[1])
    if periode[0] < 0 or (periode[0]==0 and periode[1]<=0):
        periode = (periode[0] + 24, periode[1])
    if periode[1] < 0 :
        periode = (periode[0] - 1, periode[1] + 60)
    
    return periode

print(duree((6, 0), (5, 15)))
print(duree((14, 39), (18, 45)))