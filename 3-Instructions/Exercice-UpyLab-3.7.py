# Exercice UpyLab 3.7 - Parcours : bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Dans mon casino, ma roulette comporte 13 numéros de 0 à 12 comme montrés ci-dessous :
# https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/roulette.jpg
# Le joueur a plusieurs types de paris possibles :
# il peut choisir de parier sur le numéro sortant, et dans ce cas, s’il gagne, il remporte douze fois sa mise ;
# il peut choisir de parier sur la parité du numéro sortant (pair ou impair), et dans ce cas, s’il gagne, il remporte deux fois sa mise ;
# enfin, il peut choisir de parier sur la couleur du numéro sortant (rouge ou noir), et dans ce cas aussi, s’il gagne, il remporte deux fois sa mise.
# Si le joueur perd son pari, il ne récupère pas sa mise.
# Pour simplifier, on suppose que le numéro 0 n’est ni rouge ni noir, mais est pair. Pour simplifier encore, on suppose que le joueur mise systématiquement 10 euros.
# Écrire un programme qui aide le croupier à déterminer la somme que le casino doit donner au joueur.
# Le programme lira, dans l’ordre, deux nombres entiers en entrée : le pari du joueur (représenté par un nombre entre 0 et 16, voir description plus bas), et le numéro issu du tirage (nombre entre 0 et 12). Le programme affichera alors le montant gagné par le joueur.
# Entrées pour le pari du joueur :
# nombre entre 0 et 12 : le joueur parie sur le numéro correspondant
# 13 : le joueur parie sur pair
# 14 : le joueur parie sur impair
# 15 : le joueur parie sur la couleur rouge
# 16 : le joueur parie sur la couleur noire.

# Read the player's bet and the drawn number
bet = int(input("Enter the player's bet: "))
drawn_number = int(input("Enter the drawn number: "))

# Calculate the amount won by the player
if bet >= 0 and bet <= 12:
    if bet == drawn_number:
        amount_won = 12 * 10
    else:
        amount_won = 0
elif bet == 13:
    if drawn_number % 2 == 0:
        amount_won = 2 * 10
    else:
        amount_won = 0
elif bet == 14:
    if drawn_number % 2 != 0:
        amount_won = 2 * 10
    else:
        amount_won = 0
elif bet == 15:
    if drawn_number % 2 == 0 and drawn_number != 0:
        amount_won = 2 * 10
    else:
        amount_won = 0
elif bet == 16:
    if drawn_number % 2 != 0 or drawn_number == 0:
        amount_won = 2 * 10
    else:
        amount_won = 0
else:
    amount_won = 0

# Print the amount won by the player
print("Amount won by the player:", amount_won)