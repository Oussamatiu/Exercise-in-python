import pandas as pd

clients = pd.read_csv("dataset/clients.csv")

print(clients["nom"])
print(clients[["nom" , "age" ,"ville"]])

print(clients.iloc[:3 ,:])

print(f"les clients ayant plus de 30 ans :\n{clients[clients["age"] > 30]}")

print(f"les clients ayant un salaire superieur a 6000 :\n{clients[clients["salaire"] > 6000]} ")

print(f"les clientd de casablanca :\n{clients[ clients["ville"] == "Casablanca"]}")

print(f"les femmes ayant plus de 30 ans :\n{clients[(clients["age"] > 30) & (clients["sexe"]== "F")]}")
print(f"les clients de casablanca ou rabat :\n{clients[(clients["ville"]=="Casablanca") | (clients["ville"] == "Rabat")]}")
print(f"les clients de casablanca ou rabat ou tanger :\n{clients[clients["ville"].isin(["Casablanca" , "Rabat" , "Tanger"])] }")

print(f"les clients aynat age dans 25 a 35 ans :\n{clients[clients['age'].between(25 , 35)]}")

print(f"les clients pas de casablanca :\n{clients[~(clients['ville'] == "Casablanca")]}")


print(clients.loc[3 , "age"])

print(clients.iloc[3,2])

print(clients.loc[3, ["nom" , "age"]])

print(clients.iloc[3, :])