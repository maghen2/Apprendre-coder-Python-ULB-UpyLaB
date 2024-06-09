"""
Exercice UpyLab 7.10 - Parcours : rouge
Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
Arthur nous a envoyé des statistiques produites par UpyLaB contenant des informations sur des exercices et sur des apprenants. Nous souhaitons utiliser ces informations pour classer les exercices.

Chaque jeu de données est formé de deux fichiers de type csv (produit par un tableur du type Excel ou LibreOffice) :

un fichier 'result-pass-fail.csv'

un fichier 'result-count.csv'

La structure d’un fichier “result-pass-fail-i.csv”

est la suivante :

En première ligne, nous trouvons les intitulés des exercices, chacun séparé du suivant par un caractère point-virgule “;”.

Chacune des lignes suivantes correspond aux résultats d’un apprenant : chaque ligne a le même nombre d’éléments que le nombre d’intitulés, et chaque élément vaut soit le texte 'VRAI', soit le texte 'FAUX', soit est vide (respectivement suivant que l’apprenant a validé tous les tests UpyLaB pour l’exercice correspondant, a demandé la validation par UpyLaB, mais malheureusement ce dernier a répondu par la négative, ou n’a pas encore testé l’exercice dans UpyLaB). À nouveau sur une même ligne, chaque valeur est séparée de la suivante par un caractère point-virgule “;”.

La structure du fichier “result-count-i.csv”

est similaire à celle du premier fichier, à la différence près que les textes “VRAI” ou “FAUX” sont remplacés par des nombres naturels strictement positifs donnant le nombre de fois où l’apprenant a testé son code. À nouveau l’entrée est vide si aucune validation n’a été demandée par l’apprenant.

De façon précise, la structure d’un fichier 'result-count-i.csv' est la suivante :

En première ligne, nous trouvons les intitulés des exercices, chacun séparé du suivant par un caractère point-virgule “;”.

Chacune des lignes suivantes correspond aux résultats d’un apprenant : chaque ligne a le même nombre d’éléments que le nombre d’intitulés, et chaque élément représente soit un nombre entier strictement positif, soit est vide (respectivement suivant que l’apprenant a validé ou essayé de valider les tests UpyLaB pour l’exercice correspondant ou n’a pas encore testé l’exercice dans UpyLaB). À nouveau sur une même ligne, chaque valeur est séparée de la suivante par un caractère point-virgule “;”.

Écrire un programme qui lit depuis l’entrée deux chaînes de caractères, représentant les noms des deux fichiers décrits ci-dessus (dans l’ordre, le fichier de type “result-pass-fail.csv” suivi du fichier du type “result-count.csv”), et qui imprime la liste des intitulés, un par ligne, dans l’ordre décroissant des « valeurs » calculées comme suit.

La « valeur » d’un intitulé est le nombre des « apprenants fiables » ayant réussi l’exercice correspondant.

Un « apprenant fiable » est un apprenant qui n’a jamais testé plus de dix fois chacun des codes qu’il a essayé de valider.

Par exemple, si un apprenant n’a testé que trois exercices en soumettant respectivement 1, 2 et 10 essais, il est réputé « fiable ». Si un autre apprenant a testé tous les exercices, mais en soumettant 11 essais pour l’un d’entre eux, il n’est pas considéré comme « fiable ».

Exemple
Avec le fichier result-pass-fail-0.csv contenant :

ex1;ex2;ex3
VRAI;VRAI;VRAI
VRAI;VRAI;VRAI
VRAI;FAUX;FAUX
VRAI;VRAI;VRAI
VRAI;VRAI;
FAUX;VRAI;VRAI
et le fichier result-count-0.csv contenant :

ex1;ex2;ex3
2;3;5
1;2;4
4;2;666
11;6;3
1;1;
7;7;7
le programme affiche :

ex2
ex3
ex1
En effet, les apprenants 3 et 4 ne sont pas fiables. Ainsi, la valeur de ex2 est égale à 4 ; ex1 et ex3 ont tous les deux une valeur égale à 3 mais ex3 est supérieur à ex1 dans l’ordre utf-8.

Consignes
Notez que dans cet exercice, il vous est demandé d’écrire un programme qui fera appel aux fonctions input et print.
Nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu. En particulier, il ne faut rien écrire à l’intérieur des appels à input( input() et non input("Entrer un nom de fichier : ") par exemple), ni ajouter du texte supplémentaire dans ce qui est imprimé (print(intitules) et non print("liste des intitulés :",intitules) par exemple).

Les fichiers utilisés par UpyLaB pour tester votre code sont :

https://upylab.ulb.ac.be/pub/data/result-pass-fail-0.csv

https://upylab.ulb.ac.be/pub/data/result-count-0.csv

https://upylab.ulb.ac.be/pub/data/result-pass-fail-1.csv

https://upylab.ulb.ac.be/pub/data/result-count-1.csv

En cas d’égalité, les exercices seront classés selon l’ordre décroissant UTF-8 de leurs intitulés.

Nous vous conseillons de définir des fonctions annexes que votre programme appellera.

Le nombre maximal d’essais pour être supposé « apprenant fiable », 10 ici, peut être vu comme une constante globale du programme.

Remarque
Cet exercice vous demande de lire des fichiers csv. Cela peut se faire bien entendu avec ce qui a été vu jusque là dans ce cours, mais vous pouvez aussi consulter la section 6.6 qui présente les outils spécifiques à la manipulation de ces fichiers csv.
AIDE EN CAS DE BESOIN
Conseils
Comme pour les premiers programmes que vous avez écrits lors de ce MOOC, UpyLaB va vérifier que ce qu’imprime votre code correspond exactement à ce qui est attendu. Veillez donc à ne pas ajouter d’espace superflue en fin de ligne, ni de ligne vide supplémentaire. Veillez aussi à ne pas ajouter de texte lors des appels à la fonction input.

Si rien ne marche : consultez la FAQ sur UpyLaB 6.20.
"""
