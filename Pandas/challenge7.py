import pandas as pd

produits = pd.read_csv("dataset/produits.csv")

commandes = pd.read_csv("dataset/commandes.csv")

clients = pd.read_csv("dataset/clients_commandes.csv")


clients_commandes = clients.merge(commandes , on="client_id")

clients_commandes_produits = clients_commandes.merge(produits , on="produit")

clients_commandes_Jinner = clients.merge(commandes , on="client_id" , how="inner")

clients_commandes_left = clients.merge(commandes , on = "client_id" , how ="left" , indicator=True)
clients_commandes_right = clients.merge(commandes , on = "client_id" , how ="right")
clients_commandes_outer = clients.merge(commandes , on = "client_id" , how ="outer")

print(f"----jointure_inner------\n{clients_commandes_Jinner}")

print(f"----jointure_left------\n{clients_commandes_left}")
print(f"----jointure_right------\n{clients_commandes_right}")
print(f"----jointure_outer------\n{clients_commandes_outer}")

clients_sans_commandes = clients_commandes_left[clients_commandes_left["_merge"] == "left_only"]

print(f"les clients n'ayant effectue aucune commande\n{clients_sans_commandes}")

concat_datasets = pd.concat([clients , commandes , produits], axis=1)

print(concat_datasets)

print(f"number of clients n'ayant effecture aucune commande : {clients_commandes_left['_merge'].value_counts()}")

print(f"number of clients   : {clients_commandes_produits['client_id'].nunique()}")