import pandas as pd

clients = pd.read_csv("dataset/clients_final.csv")


clients_presents = clients.shape[0]

variables_dataset = clients.shape[1]
print(f"les clients sont presents est : {clients_presents}")
print(f"les variables sont presents dans dataset est : {variables_dataset}")

print(f"la moyen de l'age est : {clients['age'].mean()}")

clients['salaire'] = clients['salaire'].str.replace("DH","").str.strip()

clients['salaire'] = pd.to_numeric(clients['salaire'], errors="coerce")
print(f"la moyen de le salaire est : {clients['salaire'].mean()}")


villes = clients['ville'].unique()

print(villes)
clients['ville'] = clients['ville'].str.strip().str.lower()
print(clients.groupby('ville').size())

print(f"les variables numeriques : {clients.select_dtypes(include="number").columns}")

print(f"les variables categorielles : {clients.select_dtypes(include="object").columns}")


print(f"les dimension est : {clients.ndim}")
print(clients.dtypes)

valeurs_manquantes = clients[clients.isna().any(axis=1)]
doublons = clients.duplicated()

clients = clients.drop_duplicates()

print(f"les valeurs_manquantes est :\n{valeurs_manquantes}")

print(f"les doublons est :\n{clients[doublons]}")

moyenne_age = clients['age'].mean()

clients['age'] = clients['age'].fillna(moyenne_age)

clients['derniere_commande'] = pd.to_datetime(clients['derniere_commande'])

print(clients)

Q1 = clients["salaire"].quantile(0.25)
Q3 = clients["salaire"].quantile(0.75)

IQR = Q3 - Q1

limite_inf = Q1 - 1.5 * IQR
limite_sup = Q3 + 1.5 * IQR

valeurs_aberrantes = clients[
    (clients["salaire"] < limite_inf) |
    (clients["salaire"] > limite_sup)
]

print(valeurs_aberrantes)

ville_plus_client = clients.groupby('ville').size().idxmax()

ville_plus_depenses = clients.groupby('ville')['depenses_totales'].sum().idxmax()

clients_plus_depensent = clients['depenses_totales'].idxmax()

nombre_moyen_commandes = clients.groupby('ville')['nombre_commandes'].mean()
print(ville_plus_client)

print(ville_plus_depenses)

print(clients.loc[clients_plus_depensent])

print(nombre_moyen_commandes)