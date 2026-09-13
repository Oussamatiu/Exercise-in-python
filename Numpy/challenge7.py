import numpy as np

salaires = np.array([30000 , 40000 , 3000 , 7000 , 43000])

moyenne = salaires.mean()

mediane = np.median(salaires)
variance = np.var(salaires)
ecart = np.std(salaires)

min_salaire = salaires.min()
max_salaire = salaires.max()

Q1 = np.percentile(salaires , 25)
Q3 = np.percentile(salaires , 75)

print("Moyenne :", moyenne)
print("Médiane :", mediane)
print("Variance :", variance)
print("Écart-type :", ecart)
print("Minimum :", min_salaire)
print("Maximum :", max_salaire)
print("1er quartile (Q1) :", Q1)
print("3ème quartile (Q3) :", Q3)
