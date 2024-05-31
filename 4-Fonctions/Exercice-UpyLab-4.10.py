import random

# Exercice UpyLab 4.10 - Parcours : bleu rouge
# Auteur Thierry Massart (Université Libre de Bruxelles)
# Pierre-feuille-ciseaux (voir Pierre-papier-ciseaux sur Wikipedia) est un jeu effectué avec les mains et opposant un ou plusieurs joueurs.

# Déroulement du jeu

# Les deux joueurs choisissent simultanément un des trois coups possibles en le symbolisant de la main :

# poing fermé : Pierre ;

# main ouverte, doigts collés les uns aux autres : Feuille ;

# main avec pouce, annulaire et auriculaire fermé, index et majeur ouvert en forme de V : Ciseaux.

# La pierre bat les ciseaux (en les émoussant), les ciseaux battent la feuille (en la coupant), la feuille bat la pierre (en l’enveloppant). Ainsi chaque coup bat un autre coup, fait match nul contre le deuxième (son homologue) et est battu par le troisième.

# Écrire un programme qui réalise 5 manches du jeu Pierre-feuille-ciseaux entre l’ordinateur et le joueur. Chaque manche va consister en :

# la génération (pseudo) aléatoire d’un nombre entre 0 et 2 compris, à l’aide de la fonction randint du module random, qui va représenter le coup de l’ordinateur (0 valant Pierre, 1, Feuille et 2, Ciseaux) ;

# la lecture en entrée (input) d’une valeur entière entre 0 et 2 compris qui représente le coup du joueur ;

# l’affichage du résultat sous une des formes :

# coup_o bat coup_j : points

# coup_o est battu par coup_j : points

# coup_o annule coup_j : points

# où

# coup_o et coup_j sont respectivement le coup de l’ordinateur et du joueur : "Pierre" s’il a joué 0, "Feuille" s’il a joué 1 et "Ciseaux" s’il a joué 2.

# points donne le résultat des manches jusqu’à présent sachant que le compteur points part de zéro, et est incrémenté de un chaque fois que le joueur gagne une manche, et décrémenté de un chaque fois que l’ordinateur gagne une manche (les match nuls ne modifiant pas le compteur points).

# À la fin des cinq manches, votre programme affichera : Perdu, Nul ou Gagné suivant que le compteur est négatif, nul ou strictement positif.

# Pour plus de clarté dans votre code, nous vous conseillons de définir les trois constantes symboliques :

# PIERRE = 0
# FEUILLE = 1
# CISEAUX = 2
# Par ailleurs, votre code doit importer le module random et, avant de commencer les manches, pour permettre à UpyLaB de valider les résultats, il doit d’abord lire une valeur entière s et appeler la fonction random.seed(s). Vous devez donc intégrer le code suivant :

# import random

# PIERRE = 0
# FEUILLE = 1
# CISEAUX = 2

# ...

# s = int(input())
# random.seed(s)
# Votre code fera donc un appel à random.seed suivi de cinq appels à random.randint, un par manche. Aucun autre appel à une fonction de random ne pourra être effectué.

# Vous pouvez bien sûr utiliser la fonction bat de l’exercice 4.9 mais nous vous conseillons vivement de définir aussi d’autres fonctions (par exemple , une fonction qui réalise une manche et imprime la ligne de message) pour structurer votre code.

PIERRE = 0
FEUILLE = 1
CISEAUX = 2


s = 65 # int(input())
random.seed(s)
points = 0 

# Écrire une fonction bat(joueur_1, joueur_2) où joueur_1 et joueur_2 ont chacun une valeur entière 0, 1 ou 2, qui encode ce que le joueur a fait comme coup (0 : PIERRE, 1 : FEUILLE, 2 : CISEAUX) qui renvoie un résultat booléen :
# vrai si joueur_1 bat le joueur_2 :
# faux si joueur_2 bat joueur_1 ou fait match nul contre lui.
def bat(joueur_1, joueur_2):
    return True if (joueur_1 == 0 and joueur_2 == 2) or (joueur_1 == 1 and joueur_2 == 0) or (joueur_1 == 2 and joueur_2 == 1) else False

# fonction qui determine l'issue de la manche en se bassant sur bat(joueur_1, joueur_2)
def jouer_manche():
    coup_nom = ["Pierre", "Feuille", "Ciseaux"]
    coup_ordinateur = random.randint(0, 2)
    coup_joueur = int(input())
    global points

    resultat = coup_nom[coup_ordinateur]+" "
    if bat(coup_ordinateur, coup_joueur):
        resultat += "bat"
        points -= 1
    elif bat(coup_joueur, coup_ordinateur):
        resultat += "est battu par"
        points += 1
    else:
        resultat += "annule"
    resultat += " "+coup_nom[coup_joueur]
    return resultat, points

# Écrire un programme qui réalise 5 manches du jeu Pierre-feuille-ciseaux entre l’ordinateur et le joueur. 
for _ in range(5):
    resultat_manche, points = jouer_manche()
    print(f"{resultat_manche} : {points}")

# À la fin des cinq manches, votre programme affichera : Perdu, Nul ou Gagné suivant que le compteur est négatif, nul ou strictement positif.
if points > 0:
    print("Gagné")
elif points < 0:
    print("Perdu")
else:
    print("Nul")