# Exercice UpyLab 4.6 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Dans cet exercice, nous allons mettre en pratique la notion de valeur par défaut des paramètres d’une fonction.
# Écrire une fonction somme(a, b) qui retourne la somme de deux valeurs entières a et b. Par défaut, la valeur de a est 0 et la valeur de b est 1.
def somme(a=0, b=1):
    return a + b