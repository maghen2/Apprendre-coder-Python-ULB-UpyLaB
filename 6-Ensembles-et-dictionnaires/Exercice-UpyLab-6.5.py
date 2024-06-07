# Exercice UpyLab 6.5 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction construction_dict_amis qui reçoit une liste de couples (prenom1, prenom2) signifiant que prenom1 déclare prenom2 comme étant son ami.

# La fonction construit et renvoie un dictionnaire dont les clés sont les prénoms des personnes nommées, et la valeur de chaque entrée est l’ensemble des amis de la personne.

# Exemple
# L’appel suivant de la fonction :

# construction_dict_amis([('Quidam', 'Pierre'),
#                         ('Thierry', 'Michelle'),
#                         ('Thierry', 'Pierre')])
# doit retourner :

# {'Quidam' : {'Pierre'}, 'Pierre' : set(), 'Thierry' : {'Michelle', 'Pierre'}, 'Michelle' : set()}

def construction_dict_amis(liste_couples):
    dict_amis = {}
    for prenom1, prenom2 in liste_couples:
        if prenom1 not in dict_amis:
            dict_amis[prenom1] = set()
        dict_amis[prenom1].add(prenom2)
        if prenom2 not in dict_amis:
            dict_amis[prenom2] = set()
    return dict_amis

liste_couples = [('Quidam', 'Pierre'), ('Thierry', 'Michelle'), ('Thierry', 'Pierre')]
result = construction_dict_amis(liste_couples)
print(result)
