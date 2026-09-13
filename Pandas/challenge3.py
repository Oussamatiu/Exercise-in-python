import pandas as pd

clients = pd.read_csv("dataset/clients_dirty.csv")

valeurs_manquantes = clients.isna().sum()

print(valeurs_manquantes)


valeurs_doublons = clients.duplicated()

print(clients[valeurs_doublons])
clients.drop_duplicates(inplace=True)

clients["nom"] = clients["nom"].str.strip()
clients["ville"] = clients["ville"].str.strip()
clients["ville"] = clients["ville"].str.lower()

clients = clients.fillna("N/A")

clients["age"] = pd.to_numeric(clients["age"], errors="coerce")

clients["salaire"] = clients["salaire"].astype(str).str.replace("DH" , "").str.replace(" ","")
clients["salaire"] = pd.to_numeric(clients["salaire"], errors="coerce")

negatif_salaires = clients["salaire"] < 0
print(clients)

print(f"les salaires negatif est :\n{clients[negatif_salaires]}")

clients.loc[clients["salaire"] < 0 , "salaire"] = pd.NA

moyenne = clients["salaire"].mean()
clients = clients.fillna(moyenne)

clients["date_inscription"] = pd.to_datetime(clients["date_inscription"] , errors="coerce")

print(clients)

print(clients.dtypes)

print(clients.shape[0])

print(f"statistique :\n{clients.describe()}")



