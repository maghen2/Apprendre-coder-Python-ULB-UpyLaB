import math

# Exercice UpyLab 2.7 - Parcours : bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire un programme qui imprime la valeur du volume d’une sphère de rayon r, float lu en entrée.

# On rappelle que le volume d’une sphère de rayon r est donné par la formule : \frac{4}{3}\pi{r^3} V = 4/3πr³.

r = float(input()
volume = (4/3) * math.pi * (r ** 3)
print(volume)