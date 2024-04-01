#Écrire un programme qui, à partir de la saisie d'un rayon et d'une hauteur, calcule le volume d'un cône droit.


def volumeCone(base, hauteur):   
    volume = float((base * hauteur* 3.14 )/3)
    return volume

base = float(input("Entrer le rayon du cone"))
hauteur = float(input("entrer la hauteur"))

print("le volume est ", round(volumeCone(base,hauteur),2), 'cm^3')

