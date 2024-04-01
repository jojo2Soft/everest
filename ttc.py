priceHTTotal = 0
choix=1
index =1
# float(input("Prix HT"))
while choix !=0:
    prix_HT_produit = input(f"Entrer Prix du produit {index} HT")

    

    # Vérifier si l'entrée est un nombre
    while not prix_HT_produit.isdigit():
        print("Veuillez entrer un nombre pour le prix.")
        prix_HT_produit = input(f"Entrez le prix du produit {index} HT : ")


    choix = int(input("Voulez-vous continuer ? (1 pour oui, 0 pour non) : "))

    index += 1
     # Ajouter le prix HT du produit au total
    priceHTTotal += float(prix_HT_produit)

priceTTC= float(priceHTTotal*0.18 +priceHTTotal )

# Afficher le résultat
print(f"Le prix total HT est : {priceHTTotal}")
print(f"Le prix total TTC est : {priceTTC}")