# Exercice UpyLab 5.21 - Parcours : bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction liste_des_mots qui reçoit en paramètre le nom d’un fichier texte, que la fonction doit ouvrir, et qui renvoie la liste des mots contenus dans le fichier.

# Consignes
# On peut supposer que le fichier est présent et dans le bon format en encodage UTF-8.

# Les mots dans la liste seront écrits en minuscule et triés dans l’ordre donné par la codification UTF-8 (en utilisant la méthode sort par exemple), les accents n’étant pas gérés de façon spécifique (« a » et « à » sont deux mots différents).

# Un même mot ne peut pas se trouver deux fois dans la liste.

# Dans le fichier source, les mots peuvent être séparés par des caractères blancs habituels (caractère espace, tabulation, passage à la ligne), ou par n’importe quel caractère parmi les suivants :

# - ' " ? ! : ; . , * = ( ) 1 2 3 4 5 6 7 8 9 0

# Certains des fichiers utilisés par UpyLaB pour tester la fonction sont accessibles aux adresses suivantes :

# https://upylab.ulb.ac.be/pub/data/Zola.txt

# https://upylab.ulb.ac.be/pub/data/le-petit-prince.txt

def liste_des_mots(nom_fichier):
    mots = []
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            mots += ligne.split()
    
    
    return mots
print(liste_des_mots("Zola.txt"))
print(liste_des_mots("le-petit-prince.txt"))