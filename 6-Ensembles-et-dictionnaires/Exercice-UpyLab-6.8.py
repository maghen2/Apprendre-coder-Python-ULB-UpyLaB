# Exercice UpyLab 6.8 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction store_email(liste_mails) qui reçoit en paramètre une liste d’adresses e-mail et qui renvoie un dictionnaire avec comme clés les domaines des adresses e-mail et comme valeurs les listes d’utilisateurs correspondantes, triées par ordre croissant (UTF-8).

# Exemple
# L’appel de la fonction suivant :

# store_email(["ludo@prof.ur", "andre.colon@stud.ulb",
#              "thierry@profs.ulb", "sébastien@prof.ur",
#              "eric.ramzi@stud.ur", "bernard@profs.ulb",
#              "jean@profs.ulb" ])
# retourne le dictionnaire :

# { 'prof.ur' : ['ludo', 'sébastien'],
#   'stud.ulb' : ['andre.colon'],
#   'profs.ulb' : ['bernard', 'jean', 'thierry'],
#   'stud.ur' : ['eric.ramzi'] }
