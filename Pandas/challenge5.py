import pandas as pd


ventes = pd.read_csv("dataset/ventes.csv")

ventes["chiffre_affaire"] = ventes["prix"] * ventes["quantite"]

print(f"le chiffre d'affaire total est {ventes['chiffre_affaire'].sum()} DH")

print(f"le chiffre d'affaires moyen est {ventes['chiffre_affaire'].mean()} DH")

print(f"le CA minimum est {ventes['chiffre_affaire'].min()} DH")

print(f"le CA maximum est {ventes['chiffre_affaire'].max()} DH")

print(f"la mediane est {ventes['chiffre_affaire'].median()} DH")

print(f"l'ecart-type est {ventes['chiffre_affaire'].std()}")

print(f"la variance est {ventes['chiffre_affaire'].var()}")

print(f"les quantiles :\nQ1 : {ventes['chiffre_affaire'].quantile(0.25)}\nQ2 : {ventes['chiffre_affaire'].quantile(0.50)}\nQ3 : {ventes['chiffre_affaire'].quantile(0.75)}")

print(f"le CA total par ville :\n{ventes.groupby("ville")["chiffre_affaire"].sum()}")

print(f"le CA moyen par ville :\n{ventes.groupby("ville")["chiffre_affaire"].mean()}")

print(f"le nombre de ventes par ville :\n{ventes.groupby("ville").size()}")

print(f"la quantite totale vendue par produit :\n{ventes.groupby("produit")["quantite"].sum()}")

print(f"le CA total par produit :\n{ventes.groupby("produit")["chiffre_affaire"].sum()}")

print(f"le produit generant le plus de CA :{ventes.groupby('produit')['chiffre_affaire'].sum().idxmax()} {ventes.groupby("produit")["chiffre_affaire"].sum().max()}")

print(ventes.groupby('produit').agg(
    total_q = ("chiffre_affaire", "sum" ),
    total_quantite = ("chiffre_affaire", "sum" ) 
))
