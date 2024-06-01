# Exercice UpyLab 5.16 - Parcours : vert bleu rouge
# Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Cet exercice peut aussi se résoudre sans utiliser la technique de compréhension de liste. Mais les solutions sont beaucoup plus courtes avec cette technique ! Nous vous demandons donc si possible de les réaliser avec du code utilisant des compréhensions de liste.

# Écrire une fonction my_pow qui prend comme paramètres un nombre entier m et un nombre flottant b, et qui renvoie une liste contenant les m premières puissances de b, c’est-à-dire une liste contenant les nombres allant de b^0 à b^{m - 1}.

# Si le type des paramètres n’est pas celui attendu, la fonction retournera la valeur None.

def my_pow(m, b):
    if not isinstance(m, int) or not isinstance(b, float):
        return None
    return [b**i for i in range(m)]

print(my_pow(3, 5.0))
print(my_pow(3.0, 5.0))
print(my_pow('a', 'b'))