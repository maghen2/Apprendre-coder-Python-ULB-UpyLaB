# Exercice UpyLab 5.19 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# D’après Wikipedia, un acrostiche est un poème, une strophe ou une série de strophes fondé sur une forme poétique consistant en ce que, lues verticalement de haut en bas, la première lettre ou, parfois, les premiers mots d’une suite de vers composent un mot ou une expression en lien avec le poème.

# Écrire une fonction acrostiche qui reçoit en paramètre le nom d’un fichier et qui retourne la chaîne de caractères formée par les premières lettres de chaque ligne du fichier.
def acrostiche(file_name):
    acrostic = ""
    with open(file_name, 'r') as file: #on ouvre le fichier
        for line in file:
            acrostic += line[0] #on recupère et cumule le premier caractère de chaque ligne
    return acrostic

print(acrostiche('Apollinaire.txt'))