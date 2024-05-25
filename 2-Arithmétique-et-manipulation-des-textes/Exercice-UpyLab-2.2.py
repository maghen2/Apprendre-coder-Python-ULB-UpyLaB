# Apprendre à coder avec Python - Université Libre de Bruxelles (ULB) UpyLaB 
# UpyLaB est une plateforme d'apprentissage en ligne permettant l'apprentissage par la pratique du langage de programmation Python
#https://upylab2.ulb.ac.be/

# Exercice UpyLab 2.2 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Le but de cet exercice est de vérifier que vous savez lire des données en entrée avec la fonction input, les affecter à des variables et imprimer (on dit aussi afficher) une valeur grâce à la fonction print.
# Écrire un programme qui imprime (donc grâce à la fonction print) la moyenne arithmétique de deux nombres de type float lus en entrée (c'est-à-dire grâce à des appels à la fonction input) .
# On rappelle que la moyenne arithmétique de deux nombres a et b est égale à  \frac{a+b}{2}.

a = float(input())
b = float(input())
average = (a + b) / 2
print(average)