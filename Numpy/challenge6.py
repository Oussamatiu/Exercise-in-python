import numpy as np

ventes = np.array([1200, 2500, 1800, 3200, 2100])

remise = 10 / 100

tva = 20 / 100

ca_remise = ventes * (1 - remise)


ca_tva = ca_remise * (1 + tva)

nombre_ventes = ventes.size

vente_moyenne = ventes.mean()


vente_min = ventes.min()

vente_max = ventes.max()

ca_total_remise = ca_remise.sum()

print("Ventes :", ventes)
print("CA après remise :", ca_remise)
print("CA avec TVA :", ca_tva)
print("Nombre de ventes :", nombre_ventes)
print("Vente moyenne :", vente_moyenne)
print("Vente minimale :", vente_min)
print("Vente maximale :", vente_max)
print("CA total après remise :", ca_total_remise)
