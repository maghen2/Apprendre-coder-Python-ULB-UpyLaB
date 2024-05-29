# Exercice UpyLab 4.7 - Parcours : bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire une fonction rac_eq_2nd_deg(a, b, c) qui reçoit trois paramètres de type float correspondant aux trois coefficients de l’équation du second degré ax^2 + bx + c = 0, avec a différent de 0, et qui renvoie la ou les solutions s’il y en a, sous forme d’un tuple.

def rac_eq_2nd_deg(a, b, c):
    delta = (b**2 - 4*a*c)**0.5
    if delta > 0:
        x2 = (-b + delta) / (2*a)
        x1 = (-b - delta) / (2*a)
        return (x1, x2)
    elif delta == 0:
        x = -b / (2*a)
        return (x,)
    else:
        return ()
    
print(rac_eq_2nd_deg(1.0,-4.0,4.0))
print(rac_eq_2nd_deg(1.0,1.0,-2.0))

