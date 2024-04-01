#Une autre boucle while : calculez la somme d'une suite de nombres positifs ou nuls.
# Comptez combien il y avait de données et combien étaient supérieures à 100.

#Entrer un nombre inférieur ou égal à 0 indique la fin de la suite.

nbs=[]
choix =1
index=1
total=0
condition=0
while choix >0:
    nb = int( input(f"entrer un nombre {index}"))

    nbs.append(nb)

    if(nb >100):
        condition +=1

    
    choix = int(int(input("Entrer un nombre inférieur ou égal à 0 indique la fin de la suite")))
    index= index+1
    
print('La somme vaut', sum(nbs), 'donnes supérieures à 100 valent', condition)

