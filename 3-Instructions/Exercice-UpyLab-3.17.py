import math

# Exercice UpyLab 3.17 - Parcours : rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# On peut calculer approximativement le sinus d’un nombre x en effectuant la sommation des premiers termes de la série (une série est une somme infinie) :

# sin(x) =  x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + ...

# où x est exprimé en radians et 3! désigne la factorielle de 3.

# Écrire un programme qui lit une valeur flottante x en entrée et imprime une approximation de sin(x)
# Cette approximation sera obtenue en additionnant successivement les différents termes de la série jusqu’à ce que la valeur du terme devienne inférieure (en valeur absolue) à une constante \epsilon que l’on fixera à 10^{-6}.
# On pourra utiliser la fonction math.factorial(n) de la bibliothèque math qui renvoie la valeur de n! (n factorielle).

x = float(input())
epsilon = 10**-6

result = x
term = x
n = 1

while abs(term) > epsilon:
    term *= -x * x / ((2 * n) * (2 * n + 1))
    result += term
    n += 1

print(result)