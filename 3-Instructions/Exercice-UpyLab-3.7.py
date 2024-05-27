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

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} est de couleur rouge")
    else:
        print(f"{numero} est de couleur bleue")
        pari = int(input("Entrez le pari du joueur : "))
        
        numero_tirage = int(input("Entrez le numéro issu du tirage : "))

        if pari >= 0 and pari <= 12:
            if pari == numero_tirage:
                montant_gagne = 12 * 10
            else:
                montant_gagne = 0
        elif pari == 13:
            if numero_tirage % 2 == 0:
                montant_gagne = 2 * 10
            else:
                montant_gagne = 0
        elif pari == 14:
            if numero_tirage % 2 != 0:
                montant_gagne = 2 * 10
            else:
                montant_gagne = 0
        elif pari == 15:
            if numero_tirage % 2 != 0 and numero_tirage != 0:
                montant_gagne = 2 * 10
            else:
                montant_gagne = 0
        elif pari == 16:
            if numero_tirage % 2 == 0 and numero_tirage != 0:
                montant_gagne = 2 * 10
            else:
                montant_gagne = 0
        else:
            montant_gagne = 0

        print(f"Le montant gagné par le joueur est de {montant_gagne} euros.")