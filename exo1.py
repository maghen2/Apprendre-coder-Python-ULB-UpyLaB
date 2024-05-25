# Apprendre à coder avec Python - Université Libre de Bruxelles (ULB) UpyLaB 
#https://www.fun-mooc.fr/en/cours/apprendre-a-coder-avec-python/
#https://upylab2.ulb.ac.be/

# Exercice 1 : Calculer la circonference et la surface d'un cercle dont l'utilisateur renseigne le rayon
import math
from math import pi
rayon = float(input("Veuillez entrer la valeur du rayon du cercle ex: 5.2 ou 3 par exemple")) # invite l'utilisateur à renseigne la valeur du rayon

circonference = rayon*2*math.pi*2
surface = rayon**2*math.pi
print("le rayon est de         : ",rayon)
print("la circonférence est de : ",circonference)
print("la surface est de       : ",surface)
