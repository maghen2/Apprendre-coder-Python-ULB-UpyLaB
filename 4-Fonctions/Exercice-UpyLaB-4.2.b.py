# Exercice UpyLaB 4.2.b - Parcours vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Attention : cet exercice est composé de l'exercice UpyLaB 4.2.a suivi en dessous de l'exercice UpyLaB 4.2.b.

# Le Petit Prince vient de débarquer sur la planète U357, et il apprend qu'il peut y voir de belles aurores boréales !


# La planète U357 a deux soleils : les étoiles E1515 et E666.  C'est pour cela que les tempêtes magnétiques sont permanentes, ce qui est excellent pour avoir des aurores boréales.

# Par contre, il y fait souvent jour, sauf bien évidemment quand les deux soleils sont couchés en même temps.

# Heureusement pour nous, une journée U357 s'écoule sur 24 heures comme sur notre Terre, et pour simplifier, nous ne prendrons pas en compte les minutes (on ne donne que les heures avec des valeurs entières entre 0 et 23). 

# Nous vous demandons d'aider le Petit Prince à déterminer les périodes de jour et de nuit.

def soleil_leve(heure_lever, heure_coucher, heure_actuelle):
    # Check if sunrise and sunset times are the same
    if heure_lever == heure_coucher:
        # Check if both times are 12 or 0
        if heure_lever in [12, 1]:
            return False
        else:
            return True
    # Check if sunrise is before sunset
    elif heure_lever < heure_coucher:
        # Check if current time is between sunrise and sunset
        if heure_lever <= heure_actuelle < heure_coucher:
            return True
    # Sunrise is after sunset
    else:
        # Check if current time is after sunrise or before sunset
        if heure_lever <= heure_actuelle or heure_actuelle < heure_coucher:
            return True
    return False

# UPYLAB 4.2B

# Il vous faut maintenant écrire un programme qui lit en entrée :

 
# . l'heure de lever du soleil E1515
# . l'heure du coucher du soleil E1515
# . l'heure de lever du soleil E666
# . l'heure du coucher du soleil E666

# et qui utilise la fonction soleil_leve pour afficher ligne par ligne chacune des heures de la journée, depuis 0 jusqu'à 23, suivies d'une espace et d'une astérisque s'il fait nuit à cette heure.

# Attention, il ne fera nuit que si E1515 et E666 sont tous deux couchés.
heure_lever_E1515 = int(input())
heure_coucher_E1515 = int(input())
heure_lever_E666 = int(input())
heure_coucher_E666 = int(input())

for heure in range(24):
    if soleil_leve(heure_lever_E1515, heure_coucher_E1515, heure) or soleil_leve(heure_lever_E666, heure_coucher_E666, heure):
        print(heure, end="\n")
    else:
        print(heure, end=" *\n")
