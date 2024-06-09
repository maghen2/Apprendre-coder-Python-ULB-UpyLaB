"""
Exercice UpyLab 7.9 - Parcours : rouge
Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
Un dictionnaire peut nous permettre de manipuler des tableaux partiellement remplis, en ne stockant que les cases non vides et en leur associant leur valeur.

Par exemple, le tableau suivant

https://upylab.ulb.ac.be/pub/static/exemple_carte.png
peut être implémenté par :

MY_PRECIOUS = 1
TRAP = -1
my_map = {}
my_map[(2,2)] = MY_PRECIOUS
my_map[(3,4)] = TRAP
my_map[(5,6)] = TRAP
my_map[(2,4)] = TRAP
my_map[(4,3)] = TRAP
Notez que les cases vides n’apparaissent pas dans le dictionnaire.

Écrire une fonction create_map(size, trapsNbr) qui reçoit deux entiers en paramètres, size, compris entre 2 et 100, et trapsNbr, de valeur strictement inférieure à size x size, et qui retourne un dictionnaire implémentant comme dans l’exemple précédent une carte de taille size et dans laquelle figurent trapsNbr cases contenant un piège (modélisé par la valeur -1) et une case contenant un trésor (modélisé par la valeur 1). L’emplacement de ces cases sera aléatoire.

Écrire une fonction play_game(map_size, treasure_map) qui reçoit un entier et une carte de taille map_size x map_size, telle que celles obtenues grâce à la fonction create_map, et qui demande à l’utilisateur d’entrer les coordonnées d’une case, jusqu’à tomber sur une case occupée. Si l’utilisateur a trouvé le trésor, la fonction retourne la valeur True, sinon l’utilisateur est tombé sur un piège et la fonction retourne False.

Exemple 1
L’appel de la fonction suivant :

create_map(4, 5)
pourrait retourner :

{(3, 1): 1, (4, 2): -1, (1, 1): -1,
 (1, 4): -1, (2, 2): -1, (4, 4): -1}
Exemple 2
L’appel de la fonction suivant :

play_game(5, {(3, 4): -1, (4, 1): 1, (2, 3): -1, (1, 5): -1})
avec les valeurs suivantes saisies en entrée :

4 2 
4 4
1 3
4 4
3 1
4 4
4 3
1 1
3 1
3 2
2 1
4 3
1 2
4 1
retourne :

True
Exemple 3
L’appel de la fonction suivant :

play_game(5, {(3, 4): -1, (4, 1): 1, (2, 3): -1, (1, 5): -1})
avec les valeurs suivantes saisies en entrée :

4 7
4 3
2 5
2 3
retourne :

False
Consignes
Dans cet exercice, il vous est demandé d’écrire seulement des fonctions. Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de ces fonctions.

Le code que vous soumettez à UpyLab ne doit rien afficher. Veillez en particulier à ne pas ajouter de paramètre lors de vos appels à input.

Notez que la numérotation des cases de la carte commence à (1, 1).

Pour la fonction create_map, pensez à utiliser le module random, et le dictionnaire retourné ne comportera que les cases occupées.

Pour la fonction play_game, les coordonnées saisies par l'utilisateur seront données sous la forme d'une série de deux entiers séparés par une espace, une case par ligne.

Pour la fonction play_game, si les valeurs saisies par le joueur ne sont pas du bon type (entières) , ni dans le bon intervalle (comprises entre 1 et map_size), ces saisies seront ignorées par le programme.

Notez enfin que les deux fonctions sont séparées et indépendantes l’une de l’autre.
"""

