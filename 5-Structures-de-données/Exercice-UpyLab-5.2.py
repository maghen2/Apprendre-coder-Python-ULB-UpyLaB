# Exercice UpyLab 5.2 - Parcours : bleu rouge
# Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier
 
# On représente un brin d’ADN par une chaîne de caractères dont les caractères sont parmi les quatre suivants : 'A' (Adénine), 'C' (Cytosine), 'G' (Guanine) et 'T' (Thymine).

# Écrire une fonction est_adn qui reçoit une chaîne de caractères en paramètre et qui retourne True si cette chaîne de caractères n'est pas vide et peut représenter un brin d’ADN, False sinon.
def est_adn(chaine):
    if chaine and all(caractere in 'ACGT' for caractere in chaine):
        return True
    else:
        return False
    
print(est_adn('ACGT'))
print(est_adn("ARTGGT"))