# Exercice UpyLab 5.6 - Parcours : vert bleu rouge
 
# Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction transcription_arn(brin_codant) qui reçoit une chaîne de caractères en paramètre, correspondant à un brin codant d'ADN, et qui retourne la chaîne de caractère représentant le brin d' ARN correspondant.

# Nous rappelons qu'un brin d'ADN peut être modélisé par une chaîne de caractères, dont les caractères sont pris parmi les quatre suivants  : 'A'(Adénine), 'C' (Cytosine),'G' (Guanine) et 'T' (Thymine).
# La transcription en ARN se traduit par le remplacement des nucléotides de Thymine par des nucléotides d'Uracile, que l'on représentera par le caractère 'U'.
# Exemple
# L’appel suivant de la fonction :

# transcription_arn('AGTCTTACCGATCCAT')
# doit retourner :

# 'AGUCUUACCGAUCCAU'
def transcription_arn(brin_codant):
    brin_arn = ""
    for nucleotide in brin_codant:
        if nucleotide == 'T':
            brin_arn += 'U'
        else:
            brin_arn += nucleotide
    return brin_arn


print(transcription_arn('AGTCTTACCGATCCAT'))