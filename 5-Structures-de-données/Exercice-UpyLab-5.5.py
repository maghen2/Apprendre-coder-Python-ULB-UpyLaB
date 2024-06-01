# Exercice UpyLab 5.5 - Parcours : bleu rouge
# Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier
 
# Écrire une fonction longueur(*points) qui reçoit en paramètres un nombre arbitraire de points (tuples de deux composantes), et retourne la longueur de la ligne brisée correspondante.
# Cette longueur se calcule en additionnant les longueurs des segments formés par deux points consécutifs.
def distance_points(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return (x**2 + y**2)**0.5

def longueur(*points):
    total_length = 0
    for i in range(len(points) - 1):
        segment_length = distance_points(points[i], points[i+1])
        total_length += segment_length
    return total_length

print(longueur((1.0, 1.0), (2.0, 1.0), (3.0, 1.0)))
print(longueur((0.5, 1.0), (2.0, 1.0), (2.5, -0.5), (-1.5, -1.0)))