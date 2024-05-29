# Exercice UpyLaB 4.2 - Parcours vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Attention : cet exercice est composé de l'exercice UpyLaB 4.2.a suivi en dessous de l'exercice UpyLaB 4.2.b.

# Le Petit Prince vient de débarquer sur la planète U357, et il apprend qu'il peut y voir de belles aurores boréales !


# La planète U357 a deux soleils : les étoiles E1515 et E666.  C'est pour cela que les tempêtes magnétiques sont permanentes, ce qui est excellent pour avoir des aurores boréales.

# Par contre, il y fait souvent jour, sauf bien évidemment quand les deux soleils sont couchés en même temps.

# Heureusement pour nous, une journée U357 s'écoule sur 24 heures comme sur notre Terre, et pour simplifier, nous ne prendrons pas en compte les minutes (on ne donne que les heures avec des valeurs entières entre 0 et 23). 

# Nous vous demandons d'aider le Petit Prince à déterminer les périodes de jour et de nuit.

# UPYLAB 4.2A

# Pour cela, vous allez dans un premier temps écrire une fonction soleil_leve qui, pour un soleil particulier, reçoit trois valeurs entières en argument pour la planète :
#      - l'heure de lever du soleil (entre 0 et 23)
#      - l'heure du coucher du soleil (entre 0 et 23)
#      - l'heure actuelle (entre 0 et 23)

# et qui renvoie une valeur booléenne vraie si le soleil est levé sur la planète à l'heure donnée en troisième argument et fausse, s'il est couché.

# On supposera que chacun des soleils ne se lève et ne se couche au plus qu'une seule fois par jour.
# Il est toutefois possible que le lever ait lieu après l'heure du coucher, ce qui signifie dans ce cas que le soleil est levé au début de la journée, puis qu'il se couche, puis qu'il se lève à nouveau plus tard dans la journée.
# Enfin, si l'heure du lever est la même que l'heure du coucher :
#      - soit toutes deux valent 12, cela signifie que le soleil ne se lève pas de la journée,
#      - soit toutes les deux valent 0, cela signifie que le soleil ne se couche pas de la journée.
# soleil_leve(6, 18, 10) # doit retourner True
# soleil_leve(15, 8, 12)  # doit retourner False
# soleil_leve(12, 12, 10) # doit retourner False
# soleil_leve(0, 0, 22) # doit retourner True

def soleil_leve(heure_lever, heure_coucher, heure_actuelle):
    # Check if sunrise and sunset times are the same
    if heure_lever == heure_coucher:
        # Check if both times are 12 or 0
        if heure_lever in [12, 0]:
            return False
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

soleil_leve(6, 18, 10) # doit retourner True
soleil_leve(15, 8, 12)  # doit retourner False
soleil_leve(12, 12, 10) # doit retourner False
soleil_leve(0, 0, 22) # doit retourner True