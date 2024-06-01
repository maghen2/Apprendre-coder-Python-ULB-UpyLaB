# Exercice UpyLab 5.8 - Parcours : vert bleu rouge
 
# Auteurs Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction prime_numbers qui reçoit comme paramètre un nombre entier nb et qui renvoie la liste des nb premiers nombres premiers.

# Si le paramètre n’est pas du type attendu, ou ne correspond pas à un nombre entier positif ou nul, la fonction renvoie None.
def prime_numbers(nb):
    if not isinstance(nb, int) or nb < 0:
        return None
    
    primes = []
    num = 2
    while len(primes) < nb: # tant que l'on n'a pas atteint le nombre requis de nombres premier on continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1): # on verifie si le nombre est premier
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    
    return primes

print(prime_numbers(4))
print(prime_numbers(-2))