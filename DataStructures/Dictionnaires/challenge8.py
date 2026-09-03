ventes = [
 {"produit": "PC", "categorie": "Informatique", "prix": 8000, "quantite": 2},
 {"produit": "Souris", "categorie": "Accessoire", "prix": 150, "quantite": 10},
 {"produit": "Clavier", "categorie": "Accessoire", "prix": 300, "quantite": 5},
 {"produit": "PC", "categorie": "Informatique", "prix": 8000, "quantite": 1},
 {"produit": "Écran", "categorie": "Informatique", "prix": 2500, "quantite": 3}
]

num_ventes = len(ventes)

chiffre = 0
for x in ventes :
    chiffre += x["prix"] * x["quantite"]
print(chiffre)
max_prix = 0
for x in ventes :
    if x["prix"] > max_prix :
        max_prix = x["prix"]
        produit = x["produit"]
print(f"Produit le plus cher est {produit}")   

quantite = 0
for x in ventes :
      quantite += x["quantite"] 

print(f"Quantité totale vendue est {quantite}")


chiffre_pr = {}
for x in ventes :
     if x["produit"] not in chiffre_pr :
        chiffre_pr[x["produit"]] = 0  

     chiffre_pr[x["produit"]] += x["prix"] * x["quantite"]

print(chiffre_pr)     

num_produit_cet = {}
produits = []
for x in ventes :
    if x["categorie"] and x["produit"] not in produits :
        if x["categorie"] not in num_produit_cet :
          num_produit_cet[x["categorie"]] = 0 
        num_produit_cet[x["categorie"]] += 1
        produits.append(x["produit"])  
print(num_produit_cet)



