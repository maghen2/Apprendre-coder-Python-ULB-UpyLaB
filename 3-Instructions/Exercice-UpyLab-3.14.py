import random

# Exercice UpyLab 3.14 - Parcours : rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Dans cet exercice, nous revenons sur le petit jeu de devinette.

# Écrire un programme qui génère de manière (pseudo) aléatoire un entier (nombre secret) compris entre 0 et 100. Ensuite, le joueur doit deviner ce nombre en utilisant le moins d’essais possible.

# À chaque tour, le joueur est invité à proposer un nombre et le programme doit donner une réponse parmi les suivantes :

# « Trop grand » : si le nombre secret est plus petit que la proposition et qu’on n’est pas au maximum d’essais

# « Trop petit » : si le nombre secret est plus grand que la proposition et qu’on n’est pas au maximum d’essais

# « Gagné en n essai(s) ! » : si le nombre secret est trouvé

# « Perdu ! Le secret était nombre » : si le joueur a utilisé six essais sans trouver le nombre secret.

# Generate a random number between 0 and 100
secret_number = random.randint(0, 100)

# Initialize the number of attempts
attempts = 1

# Loop until the player guesses the secret number or reaches the maximum number of attempts
while attempts <= 6:
    
    guess = int(input()) # Read the player's guess

    # Check if the guess is too high
    if guess > secret_number:
        print("Trop grand")
    # Check if the guess is too low
    elif guess < secret_number:
        print("Trop petit")
    # The guess is correct
    else:
        print("Gagné en", attempts, "essai(s) !")
        break
    
    attempts += 1 # Increment the number of attempts

# The player didn't guess the secret number within the maximum number of attempts
if attempts > 6 :
    print("Perdu ! Le secret était", secret_number)  
elif guess == secret_number 
    print("Gagné en", attempts, "essai(s) !")
