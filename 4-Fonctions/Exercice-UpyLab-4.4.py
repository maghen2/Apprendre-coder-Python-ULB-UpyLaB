import random

# Exercice UpyLab 4.4 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction alea_dice(s) qui génère trois nombres (pseudo) aléatoires à l’aide de la fonction randint du module random, représentant trois dés (à six faces avec les valeurs de 1 à 6), et qui renvoie la valeur booléenne True si les dés forment un 421, et la valeur booléenne False sinon.

# Le paramètre s de la fonction est un nombre entier, qui sera passé en argument à la fonction random.seed au début du code de la fonction. Cela permettra de générer la même suite de nombres aléatoires à chaque appel de la fonction, et ainsi de pouvoir tester son fonctionnement.
def alea_dice(s):
    random.seed(s)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    #print(dice1, dice2, dice3)

    if dice1 != dice2 and dice1 != dice3 and dice2 != dice3 and dice1 in [4, 2, 1] and dice2 in [4, 2, 1] and dice3 in [4, 2, 1]:
        return True
    else:
        return False
    
print(alea_dice(1)) # doit retourner False
print(alea_dice(25)) # doit retourner True