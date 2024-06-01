# Exercice UpyLab 5.15 - Parcours : rouge
# Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier, Jacky Trinh
# Afin de l’aider, nous vous demandons d’écrire une fonction correcteur(mot, liste_mots) où mot est le mot que Joao écrit et liste_mots est une liste qui contient les mots (ayant la bonne orthographe) que Joao est susceptible d’utiliser.

# Cette fonction doit retourner le mot dont l’orthographe a été corrigée.

def distance_mots(mot_1, mot_2):
    distance = 0
    taille = len(mot_1)
    if taille > len(mot_2):
        taille = len(mot_2)

    for i in range(taille):
        if mot_1[i] != mot_2[i]:
            distance += 1
    return distance

def correcteur(mot, liste_mots): # On part du postulat que le premier mot est le mot correct
 
    for i in range(1, len(liste_mots)): # Ensuite on compare la distance entre le premier mot et les autres mots de la liste
        if (len(mot)-len(liste_mots[i])) in range(-1, 2):
            if distance_mots(mot, liste_mots[i]) <= 1:
                mot_correct = liste_mots[i]

    return mot_correct

print(correcteur("chat", ["chien", "chat", "train", "voiture", "bonjour", "merci"]))
print(correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"]))
