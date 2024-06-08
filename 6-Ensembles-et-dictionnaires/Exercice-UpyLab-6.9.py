# Exercice UpyLab 6.9 - Parcours : bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction compteur_lettres(texte) qui renvoie un dictionnaire contenant toutes les lettres de l’alphabet associées à leur nombre d’apparition dans texte.

# Exemple
# L’appel de la fonction suivant :

# compteur_lettres("Dessine-moi un mouton !")
# retourne :

# {'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 2,
#  'f': 0, 'g': 0, 'h': 0, 'i': 2, 'j': 0,
#  'k': 0, 'l': 0, 'm': 2, 'n': 3, 'o': 3,
#  'p': 0, 'q': 0, 'r': 0, 's': 2, 't': 1,
#  'u': 2, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
#  'z': 0}

def compteur_lettres(texte):
    compteur = {}
    for lettre in texte:
        if lettre.isalpha():
            lettre = lettre.lower()
            if lettre in compteur:
                compteur[lettre] += 1
            else:
                compteur[lettre] = 1
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for lettre in alphabet:
        if lettre not in compteur:
            compteur[lettre] = 0
    return compteur

compteur_lettres("Dessine-moi un mouton !")