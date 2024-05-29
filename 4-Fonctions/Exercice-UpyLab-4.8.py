# Exercice UpyLab 4.8 - Parcours : bleu rouge
# Auteur Thierry Massart (Université Libre de Bruxelles)
# De Wikipedia (5 février 2019) :

# En mathématiques, et plus particulièrement en combinatoire, les nombres de Catalan forment une suite d’entiers naturels utilisée dans divers problèmes de dénombrement.

# Ils sont nommés ainsi en l’honneur du mathématicien belge Eugène Charles Catalan (1814-1894).

# Les dix premiers nombres de Catalan (pour n de 0 à 9) sont :

# 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862.

# Le nombre de Catalan d’indice n, appelé n-ième nombre de Catalan, est défini par :

# C_n = \frac{(2n)!}{(n+1)!n!}

# où n! désigne la factorielle de la valeur entière n :

# n! = n(n-1)(n-2)...1

# Par exemple, 5! = 5.4.3.2.1 = 120 et

# C_4 = \frac{8!}{5! 4!} = 14

# Le nombre de chemins sous-diagonaux les plus courts dans une grille de taille {n}\times{n}, le nombre de façons de découper en triangles un polygone convexe à n+2 côtés, ou encore le nombre de configurations possibles d’expressions avec n paires de parenthèses, appelé également mot de Dyck de longueur 2n, sont des exemples dont le résultat est donné par le nombre de Catalan C_n.

# Exemples d’applications de \mathbf{C_n} (ici, n = 4)

# Nombre de chemins sous-diagonaux les plus courts dans une grille de taille {n}\times{n}

# https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/chemins.jpg
# Nombre de façons de découper en triangles un polygone convexe de taille n + 2

# https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/catalan_hexagone.jpg
# Nombre de parenthésages possibles (mots de Dyck)

# (((())))

# ((()()))

# ((())())

# (()(()))

# ()((()))

# (()()())

# ((()))()

# ()(()())

# (())(())

# (()())()

# (())()()

# ()(())()

# ()()(())

# ()()()()


# Nous vous demandons d’écrire une fonction catalan(n), où n est un nombre entier positif ou nul, qui renvoie la valeur du  n-ième nombre de Catalan.