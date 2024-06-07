# Exercice UpyLab 6.4 - Parcours : bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Lors de prises de notes, il nous arrive souvent de remplacer des mots par des abréviations (bonjour est remplacé par bjr par exemple).

# Nous allons utiliser un dictionnaire qui associe à chacune de ces abréviations sa signification.

# Écrire une fonction substitue(message, abreviation) qui renvoie une copie de la chaîne de caractères message dans laquelle les mots qui figurent parmi les clés du dictionnaire abreviation sont remplacés par leur signification (valeur).

# Exemple
# L’appel suivant de la fonction :

# substitue('C. N. cpt 2 to inf', {'C.' : 'Chuck',
#                                  'N.' : 'Norris',
#                                  'cpt' : 'counted',
#                                  '2' : 'two times',
#                                  'inf' : 'infinity'})
# doit retourner :

# 'Chuck Norris counted two times to infinity'

def substitue(message, abreviation):
    words = message.split()  # Split the message into individual words
    result = []  # Create an empty list to store the substituted words
    for word in words:
        if word in abreviation:
            result.append(abreviation[word])  # Replace the word with its corresponding value from the abbreviation dictionary
        else:
            result.append(word)  # Keep the word as it is if it is not found in the abbreviation dictionary
    return ' '.join(result)  # Join the substituted words back into a single string with spaces in between


resultat = substitue('C. N. cpt 2 to inf', {'C.' : 'Chuck',
                                'N.' : 'Norris',
                                'cpt' : 'counted',
                                '2' : 'two times',
                                'inf' : 'infinity'})
print(resultat)  # Chuck Norris counted two times to infinity
