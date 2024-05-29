# Exercice UpyLab 4.5 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Considérons les billets et pièces de valeurs suivantes : 20 euros, 10 euros, 5 euros, 2 euros et 1 euro.
# Écrire une fonction rendre_monnaie qui reçoit en paramètre un entier prix et cinq valeurs entières x20, x10, x5, x2 et x1, qui représentent le nombre de billets ou de pièces de chaque valeur que donne un client pour l’achat d’un objet dont le prix est mentionné.

# La fonction doit renvoyer cinq valeurs, représentant le nombre de billets et pièces de chaque sorte qu’il faut rendre au client, dans le même ordre que précédemment. Cette décomposition doit être faite en rendant le plus possible de billets et pièces de grosses valeurs.

# Si la somme d’argent avancée par le client n’est pas suffisante pour effectuer l’achat, la fonction retournera cinq valeurs None.
def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    paiement = x20 * 20 + x10 * 10 + x5 * 5 + x2 * 2 + x1
    if total_avance < prix:
        return None, None, None, None, None
    
    montant_rendu = total_avance - prix
    rendu_20 = montant_rendu // 20
    montant_rendu %= 20
    rendu_10 = montant_rendu // 10
    montant_rendu %= 10
    rendu_5 = montant_rendu // 5
    montant_rendu %= 5
    rendu_2 = montant_rendu // 2
    montant_rendu %= 2
    rendu_1 = montant_rendu
    
    return rendu_20, rendu_10, rendu_5, rendu_2, rendu_1