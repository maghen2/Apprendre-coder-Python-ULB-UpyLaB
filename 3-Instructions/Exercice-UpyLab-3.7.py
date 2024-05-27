# Exercice UpyLab 3.7 - Parcours : bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Dans mon casino, ma roulette comporte 13 numéros de 0 à 12 comme montrés ci-dessous :

# https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/roulette.jpg
# Roulette

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} est de couleur rouge")
    else:
        print(f"{numero} est de couleur bleue")
