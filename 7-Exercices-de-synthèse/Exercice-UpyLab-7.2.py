# Exercice UpyLab 7.2 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction belongs_to_file(word, filename) qui reçoit deux chaînes de caractères en paramètre. La première correspond à un mot, et la deuxième au nom d’un fichier contenant une liste de mots, chacun sur sa propre ligne. La fonction vérifie si le mot figure dans cette liste, et retourne True si c’est bien le cas, False sinon.

# Exemple
# L’appel de la fonction suivant, où words.txt est le fichier indiqué dans les consignes ci-dessous et en supposant qu'il se trouve dans le même répertoire que le programme :

# belongs_to_file("renard", "words.txt")
# retourne :

# False
# Consignes
# Dans cet exercice, il vous est demandé d’écrire seulement la fonction belongs_to_file. Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

# Vous pourrez supposer que le fichier passé en paramètre contient bien une liste de mots, chacun sur sa propre ligne.

# N’oubliez pas d’ouvrir le fichier dans le code de la fonction.

# Le fichier utilisé par UpyLaB pour effectuer les tests est disponible à l’adresse :

# https://upylab.ulb.ac.be/pub/data/words.txt
# AIDE EN CAS DE BESOIN
# Conseils
# N’oubliez pas d’ôter le caractère de fin de ligne lorsque vous voulez comparer les deux chaînes de caractères.
def belongs_to_file(word, filename):
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() == word:
                return True
    return False

# Test
print(belongs_to_file("renard", "words.txt")) # False

