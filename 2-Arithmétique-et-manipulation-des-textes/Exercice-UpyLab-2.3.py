# Apprendre à coder avec Python - Université Libre de Bruxelles (ULB) UpyLaB 
# UpyLaB est une plateforme d'apprentissage en ligne permettant l'apprentissage par la pratique du langage de programmation Python
#https://upylab2.ulb.ac.be/

# Exercice UpyLab 2.3 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
#  Le but de cet exercice est de vous familiariser avec la lecture (input()) de données et l’impression (print()) de résultats.

# Une méthode pour trouver le quatrième terme parmi quatre termes ayant un même rapport de proportion \frac{a}{b} = \frac{c}{d} lorsque trois de ces termes sont connus repose sur l'égalité des produits en croix.

# Elle utilise le fait que le produit des premier et quatrième termes est égal au produit du second et du troisième : a.d = b.c et donc d = \frac{b.c}{a}

# Exemple : si chacun mange autant de chocolat et que pour 4 personnes il en faut 100 grammes, pour 7 personnes il en faudra donc d tel que \frac{4}{100} = \frac{7}{d}

# D’où d = \frac{7.100}{4} grammes = 175 grammes.

# Écrire un programme qui lit des valeurs de type float pour a, b et c et qui affiche la valeur de d vérifiant l'égalité \frac{a}{b} = \frac{c}{d}.

a = float(input())
b = float(input())
c = float(input())
d = (b * c) / a
print(d)
