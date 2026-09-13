import pandas as pd

employes = pd.read_csv("dataset/employes.csv")

print(f"le salaire moyen par departement :\n{employes.groupby('departement')['salaire'].mean()}")

employes['salaire_moyen_departement'] = employes.groupby('departement')['salaire'].transform("mean")

ecart_au_salaire = (
    employes["salaire"] 
    - employes["salaire_moyen_departement"]
)

employes['ecart_au_salaire'] = ecart_au_salaire

print(ecart_au_salaire)


print(f"la performance moyenne par departement :\n{employes.groupby('departement')['performance'].mean()}")

employes['performance_moyenne_departement'] = employes.groupby('departement')['performance'].transform("mean")

print(employes)

print(f"les employes ayant un salaire superieur a la moyenne de leur departement : \n{employes[employes['salaire'] > employes['salaire_moyen_departement']]}")

print(employes['departement'].agg(
    num_departement = "nunique",
    number_employees = "count"
))

print(employes.groupby('departement').agg(
    numbers_employees_departement = ("departement" , "count")
))

def category_salaire(salaire):
    if salaire < 3000:
        return "Faible"
    elif salaire <= 7000:
        return "Moyen"
    else:
        return "Élevé"

employes['category_salaire'] = employes['salaire'].apply(category_salaire)

print(employes)
  
