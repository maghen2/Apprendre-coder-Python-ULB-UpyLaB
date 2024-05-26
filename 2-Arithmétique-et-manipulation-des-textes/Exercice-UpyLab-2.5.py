# Exercice UpyLab 2.5 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Le but de cet exercice est de vous familiariser avec la syntaxe Python pour écrire des expressions arithmétiques simples et avec l’instruction print qui affiche (on dit aussi imprime) des valeurs à l’écran.

# Écrire un programme qui lit deux valeurs entières x et y strictement positives suivies de deux valeurs réelles (float) z et t, et qui affiche les valeurs des expressions suivantes, chacune sur une nouvelle ligne :

# x - y

# x + z

# z + t

# x.z        (soit le produit de x et de z)

# \frac{x}{2}

# \frac{x}{y + 1}

# x^{-\frac{1}{2}}       (soit x à la puissance d'exposant -1/2)

x = int(input())
y = int(input())
z = float(input())
t = float(input())

print(x - y)
print(x + z)
print(z + t)
print(x * z)
print(x / 2)
print(x / (y + 1))
print(((x+y)*z)/(4*x))
print(x ** (-1/2))