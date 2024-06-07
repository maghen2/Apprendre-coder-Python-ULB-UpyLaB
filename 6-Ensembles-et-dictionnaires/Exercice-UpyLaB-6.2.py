# Exercice UpyLaB 6.2 - Parcours vert bleu rouge
# Auteurs: Sébastien Hoarau, Thierry Massart, Isabelle Poirier, Jacky Trinh

# Monsieur Germain est une personne très âgée. Il aimerait préparer une liste de courses à faire à l’avance. Ayant un budget assez serré, il voudrait que sa liste de courses soit dans ses capacités. Son seul petit souci est qu’il a une très mauvaise vue et n’arrive donc pas à voir le prix associé à chaque produit contenu dans le catalogue de courses.

# Écrire une fonction calcul_prix(produits, catalogue) où :

# produits est un dictionnaire contenant, comme clés, les produits souhaités par Monsieur Germain et comme valeurs associées, la quantité désirée de chacun d’entre eux,

# catalogue est un dictionnaire contenant tous les produits du magasin avec leur prix associé.

# La fonction retourne le montant total des achats de Monsieur Germain.

# Exemple
# L’appel suivant de la fonction :

# calcul_prix({"brocoli":2, "mouchoirs":5, "bouteilles d'eau":6},
#             {"brocoli":1.50, "bouteilles d'eau":1, "bière":2,
#              "savon":2.50, "mouchoirs":0.80})
# doit retourner :

# 13.0
def calcul_prix(produits, catalogue):
    total = 0
    for produit, quantite in produits.items():
        if produit in catalogue:
            prix = catalogue[produit]
            total += prix * quantite
    return total


produits = {"brocoli":2, "mouchoirs":5, "bouteilles d'eau":6}
catalogue = {"brocoli":1.50, "bouteilles d'eau":1, "bière":2, "savon":2.50, "mouchoirs":0.80}
result = calcul_prix(produits, catalogue)
print(result)
