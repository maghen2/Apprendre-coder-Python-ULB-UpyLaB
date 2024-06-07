# Exercice UpyLab 6.3 - Parcours : bleu rouge
# Auteurs: Sébastien Hoarau, Thierry Massart, Isabelle Poirier, Jacky Trinh
# Un jury doit attribuer le prix du « Codeur de l’année ».

# Afin de récompenser les trois candidats ayant obtenu la meilleure moyenne, nous vous demandons d’écrire une fonction top_3_candidats(moyennes) qui reçoit un dictionnaire contenant comme clés les noms des candidats et comme valeurs la moyenne que chacun a obtenue.

# Cette fonction doit retourner un tuple contenant les noms des trois meilleurs candidats, par ordre décroissant de leurs moyennes.

# Exemple
# L’appel suivant de la fonction :

# top_3_candidats({'Candidat 7': 2, 'Candidat 2': 38, 'Candidat 6': 85,
#                  'Candidat 1': 8, 'Candidat 3': 17, 'Candidat 5': 83,
#                  'Candidat 4': 33})
# doit retourner :

# ('Candidat 6', 'Candidat 5', 'Candidat 2')
def top_3_candidats(moyennes):
    sorted_candidats = sorted(moyennes.items(), key=lambda x: x[1], reverse=True)
    top_3 = [candidat[0] for candidat in sorted_candidats[:3]]
    return tuple(top_3)

moyennes = {'Candidat 7': 2, 'Candidat 2': 38, 'Candidat 6': 85,
            'Candidat 1': 8, 'Candidat 3': 17, 'Candidat 5': 83,
            'Candidat 4': 33}
result = top_3_candidats(moyennes)
print(result)
