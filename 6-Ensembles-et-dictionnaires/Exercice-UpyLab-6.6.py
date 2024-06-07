# Exercice UpyLab 6.6 - Parcours : rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction symetrise_amis qui reçoit un dictionnaire d d’amis où les clés sont des prénoms et les valeurs, des ensembles de prénoms représentant les amis de chacun.

# Cette fonction modifie le dictionnaire d de sorte que si une clé prenom1 contient prenom2 dans l’ensemble de ses amis, l’inverse soit vrai aussi.

# La fonction accepte un second paramètre englobe.

# Si englobe est vrai, la fonction ajoutera les éléments nécessaires pour symétriser le dictionnaire d.

# Sinon, la fonction enlèvera les éléments nécessaires pour symétriser d.

# Exemple 1
# L’exécution du code suivant :

# d = {'Thierry': {'Michelle', 'Bernadette'},
#      'Michelle': {'Thierry'},
#      'Bernadette': set()}
# symetrise_amis(d, True)
# print(d)
# doit afficher, à l’ordre près :

# {'Thierry': {'Michelle', 'Bernadette'},
#  'Michelle' : {'Thierry'},
#  'Bernadette' : {'Thierry'}}
# Exemple 2
# L’exécution du code suivant :

# d = {'Thierry': {'Michelle', 'Bernadette'},
#      'Michelle': {'Thierry'},
#      'Bernadette': set()}
# symetrise_amis(d, False)
# print(d)
# doit afficher, à l’ordre près :

# {'Thierry': {'Michelle'},
#  'Michelle' : {'Thierry'},
#  'Bernadette' : set()}

def symetrise_amis(d, englobe):
    for prenom1, amis in d.items():
        for prenom2 in amis.copy():
            if prenom2 not in d or prenom1 not in d[prenom2]:
                if englobe:
                    d.setdefault(prenom2, set()).add(prenom1)
                else:
                    amis.remove(prenom2)

d = {'Thierry': {'Michelle', 'Bernadette'},
     'Michelle': {'Thierry'},
     'Bernadette': set()}
symetrise_amis(d, True)
print(d)

d = {'Thierry': {'Michelle', 'Bernadette'},
     'Michelle': {'Thierry'},
     'Bernadette': set()}
symetrise_amis(d, False)
print(d)