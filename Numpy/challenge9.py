import numpy as np

ventes = np.array([[2 , 5 , 10 , 43 ],
                   [100 , 300 , 30 , 203],
                   [300 , 1 , 40 , 400]])

ventes_total = ventes.sum()

moyenne_produits = ventes.mean(axis= 1)

ventes_total_mois = ventes.sum(axis = 0)

moyenne_mois = ventes.mean(axis = 0)

meilleur_produit = np.argmax(ventes.sum(axis = 1))

meilleur_mois = np.argmax(ventes.sum(axis = 0))
print(f"les ventes totales est {ventes_total}")
print(f"les moyenne de produits : {moyenne_produits}")
print(f"les ventes total par mois : {ventes_total_mois}")
print(f"le meilleur produit est {meilleur_produit + 1}")
print(f"le meilleur mois est {meilleur_mois + 1}")

