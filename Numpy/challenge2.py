import numpy as np

periode = np.array([10 , 20 , 12 , 50 , 50])
temperatures = np.arange(5 , 50)
prixs = np.linspace(100 , 1000, num = 7 , dtype=int)
produits = np.array(["produit 1" , "pro 2" , "pro 3" , "pro 4" , "pro 5" , "pro 6" , "pro 7"])

print(np.array_equal(prixs , periode)) 

print(prixs)