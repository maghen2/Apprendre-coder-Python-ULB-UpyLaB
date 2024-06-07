# Exercice UpyLab 6.7 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction prime_odd_numbers(numbers) qui reçoit une liste de nombres et qui renvoie un couple d’ensembles contenant respectivement les nombres premiers présents dans la liste et les nombres impairs.

# Pour cela, nous vous demandons d’écrire au préalable deux fonctions annexes qui seront appelées dans le corps de la fonction prime_odd_numbers :

# la fonction even qui accepte un nombre entier en paramètre et renvoie l’ensemble des nombres naturels pairs qui lui sont inférieurs ou égaux

# la fonction prime_numbers qui accepte un nombre entier en paramètre et renvoie l’ensemble des nombres premiers qui lui sont inférieurs ou égaux.

# Exemple 1
# L’appel de la fonction suivant :

# prime_odd_numbers([1, 2, 6, 5, 11, 9, 13, 14, 12, 15, 17, 18])
# retourne, à l’ordre près, :

# ({2, 5, 11, 13, 17}, {1, 5, 11, 9, 13, 15, 17})
# Exemple 2
# L’appel de la fonction suivant :

# prime_odd_numbers([1, 4, 6, 12, 9, 15, 16, 21, 18])
# retourne, à l’ordre près, :

# (set(), {1, 9, 15, 21})
def prime_odd_numbers(numbers):
    def even(n):
        return set(i for i in range(n+1) if i % 2 == 0)
    
    def prime_numbers(n):
        primes = set()
        for i in range(2, n+1):
            if all(i % j != 0 for j in range(2, int(i**0.5)+1)):
                primes.add(i)
        return primes
    
    primes = prime_numbers(max(numbers))
    odds = set(i for i in numbers if i % 2 != 0)
    
    return primes, odds

print(prime_odd_numbers([1, 2, 6, 5, 11, 9, 13, 14, 12, 15, 17, 18]))
print(prime_odd_numbers([1, 4, 6, 12, 9, 15, 16, 21, 18]))