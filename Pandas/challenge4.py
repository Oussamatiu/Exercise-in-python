import pandas as pd

ventes = pd.read_csv("dataset/ventes.csv")

ventes["chiffer_affaire"] = (ventes["prix"] * ventes["quantite"])



ventes["prix_avec_tva"] = ventes["prix"] * 1.2

ventes["categorie_prix"] = "incun"

ventes.loc[ventes["chiffer_affaire"] < 1000 , "categorie_prix"] = "Faible"

ventes.loc[ (ventes["chiffer_affaire"] <= 5000) & (ventes["chiffer_affaire"] >= 1000), "categorie_prix"] = "Moyen"

ventes.loc[ventes["chiffer_affaire"] > 5000 , "categorie_prix"] = "Eleve"


ventes["total_tva"] = ventes["chiffer_affaire"] * 0.2


print(ventes)