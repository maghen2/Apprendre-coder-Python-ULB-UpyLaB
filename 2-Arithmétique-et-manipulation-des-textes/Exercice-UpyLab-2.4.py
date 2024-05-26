import math

# Exercice UpyLab 2.4 - Parcours : bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire un programme qui lit une longueur long de type float strictement positive, et qui affiche les valeurs x y des coordonnées (x, y) des sommets de l’hexagone de centre (0,0) et de rayon long
# Chaque couple de coordonnées sera affiché sur une ligne différente, en commençant par le point à 0°, puis par le point à 60°, puis 120° … jusqu’au 6ème point.

long = float(input())

for i in range(6):
    angle = i * 60
    x = long * math.cos(math.radians(angle))
    y = long * math.sin(math.radians(angle))
    print(f"{x} {y}")
    