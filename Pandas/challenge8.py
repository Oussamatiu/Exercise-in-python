import pandas as pd

ventes_dates = pd.read_csv("dataset/ventes_dates.csv")

ventes_dates['date'] = pd.to_datetime(ventes_dates['date'])

print(ventes_dates['date'].dtype)

print(ventes_dates['date'].dt.year)
print(ventes_dates['date'].dt.month)
print(ventes_dates['date'].dt.day)

print(ventes_dates['date'].dt.day_name())
print(ventes_dates['date'].dt.quarter)

ventes_dates['CA'] = ventes_dates['montant'] * ventes_dates['quantite']

CA_mois = ventes_dates.groupby(ventes_dates['date'].dt.month)["CA"].sum()

CA_trimester = ventes_dates.groupby(ventes_dates['date'].dt.quarter)["CA"].sum()

print(CA_mois)

print(CA_trimester)

print(ventes_dates.groupby(ventes_dates['date'].dt.month)["CA"].sum().idxmax())


pivot_table = pd.pivot_table(ventes_dates,
                             index="produit",
                             columns="ville",
                             values="CA",
                             aggfunc="sum"
                          )
print(pivot_table)

cross_tab = pd.crosstab(ventes_dates['produit'], ventes_dates['ville'])


print(cross_tab)
ventes_dates["date"] = pd.to_datetime(ventes_dates["date"])

ventes_dates = ventes_dates.set_index("date")
print(ventes_dates['CA'].resample("ME").sum())

ventes_villes = (ventes_dates.groupby("ville")["CA"].resample("ME").sum().reindex())

print(ventes_villes)