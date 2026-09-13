import pandas as pd


clients = pd.read_csv("dataset/clients.csv")

premieres_lingnes = clients.head(5)

print(f"les premieres lingnes :\n{premieres_lingnes}")

print(f"les dernieres lingnes :\n{clients.tail(5)}")


nombre_colonnes = len(clients.columns)

print(f"nomber de lignes est {clients.shape[0]}\nnomber de colonnes est {nombre_colonnes}")

print(f"les noms des colonnes est : {clients.columns}")

print(f"l'index est : {clients.index.tolist()}")

print(f"les types de donnes est {clients.dtypes}")

clients.info()
print("_____________________")
print(clients.describe())

numerique_colonnes = clients.select_dtypes(include="number").columns
categorielles_colonnes = clients.select_dtypes(include="object").columns

print(f"les colonnes numeriques est : {numerique_colonnes}")
print(f"les colonnes categorielle est : {categorielles_colonnes}")

print(f"les valeurs uniques de ville est : \n{clients["ville"].unique()}")

print(f"le nombre de villes differentes est : {clients['ville'].nunique()}")


print(f"le nomber de clients par ville :\n{clients['ville'].value_counts()}")

print(f"les valeurs manquantes est : {clients.isna()}")
