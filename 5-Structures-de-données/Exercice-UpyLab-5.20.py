# Exercice UpyLab 5.20 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction nouveaux_heros dont le but consiste à remplacer les héros d'une histoire.

# La fonction acceptera deux paramètres :
# le premier sera une chaîne de caractères précisant le nom du fichier contenant l'histoire initiale ;
# le deuxième sera une chaîne de caractères précisant le nom du fichier dans lequel sera sauvegardée l'histoire modifiée comme précisé ci-dessous.

# Dans l'histoire initiale, présente dans le fichier dont le nom est donné en premier argument, trois protagonistes interviennent : Pierre, Paul et Jacqueline.
# La fonction devra remplacer ces trois héros par, respectivement, Paul, Tom et Mathilde.
# Le texte ainsi modifié sera alors stocké dans le fichier dont le nom est donné en deuxième argument.
# Aucune autre modification ne sera apportée au texte initial.

# Exemple
# Sachant que le fichier histoire_1.txt contient le texte :

# Si Pierre est le fils de Paul, et si Paul est le frère de Jacqueline, qui est Pierre pour Jacqueline ?
# après l'appel suivant de la fonction :

# nouveaux_heros("histoire_1.txt", "nouvelle_histoire_1.txt")
# le fichier dont le nom est nouvelle_histoire_1.txt doit contenir le texte :

# Si Paul est le fils de Tom, et si Tom est le frère de Mathilde, qui est Paul pour Mathilde ?