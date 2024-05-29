# Exercice UpyLab 3.8 - Parcours : rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Les cinq polyèdres réguliers de Platon sont représentés ci-dessous, avec la formule de leur volume.
# Source des images de polyèdres : Vikidia, l’encyclopédie pour les jeunes, qui explique aux enfants et à ceux qui veulent une présentation simple d'un sujet (https://fr.vikidia.org/wiki/Polyèdre).  
# Nom
# Volume
# Image
# Tétraèdre
# \frac{\sqrt{2}}{12}a^3
# https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/Tetraedre.gif
# Cube
# a^3
# https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/cube.gif
# Octaèdre
# \frac{\sqrt{2}}{3}a^3
# https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/octaedre.gif
# Dodécaèdre
# \frac{15 + 7\sqrt{5}}{4}a^3
# https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/dodecaedre.gif
# Icosaèdre
# \frac{5(3 + \sqrt{5})}{12}a^3
# https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/icosaedre.gif
# Écrire un programme qui lit :
# la première lettre en majuscule du nom du polyèdre ("T", "C", "O", "D" ou "I"),
# la longueur de l’arête du polyèdre,
# et qui imprime le volume du polyèdre correspondant.
# Si la lettre lue ne fait pas partie des cinq initiales, le programme imprime le message "Polyèdre non connu".
# Exemple 1
# Avec les données lues suivantes :
# C
# 2.0
# le résultat à imprimer vaudra :
# 8.0
# Exemple 2
# Avec les données lues suivantes :
# I
# 2.0
# le résultat à imprimer vaudra (approximativement) :
# 17.4535599249993
# Exemple 3
# Avec les données lues suivantes :
# A
# 2.0
# le résultat à imprimer vaudra :
# Polyèdre non connu
polyhedron = input() # Read the polyhedron's name
edge_length = float(input()) # Read the edge length of the polyhedron

if polyhedron == "T":
    volume = (2 ** 0.5 / 12) * edge_length ** 3
elif polyhedron == "C":
    volume = edge_length ** 3
elif polyhedron == "O":
    volume = (2 ** 0.5 / 3) * edge_length ** 3
elif polyhedron == "D":
    volume = ((15 + 7 * 5 ** 0.5) / 4) * edge_length ** 3
elif polyhedron == "I":
    volume = (5 * (3 + 5 ** 0.5) / 12) * edge_length ** 3
else:
    volume = "Polyèdre non connu"

print(volume)