# Exercice UpyLab 5.4 - Parcours : vert bleu rouge
# Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier
 
# Écrire une fonction distance_points() qui reçoit en paramètres deux tuples de deux composantes représentant les coordonnées de deux points et qui retourne la distance euclidienne séparant ces deux points.
# Pour rappel, la distance euclidienne entre les points (x_1, y_1) et (x_2, y_2) se calcule grâce à la formule :

# dist = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}

# où, si a désigne un nombre positif, \sqrt{a} désigne la racine carrée de a et correspond à a^{\frac{1}{2}}.
def distance_points(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return (x**2 + y**2)**0.5

print(distance_points((-1.0, 0.5), (2.0, 1.0)))