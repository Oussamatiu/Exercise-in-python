import numpy as np

clients = np.array([[20 , 200000 , 50 , 4000],[45 , 3490000, 19 , 54300],[32 , 400000 , 10 , 100000],[32 , 400000 , 10 , 100000]])


print(f"age de client {clients[0 , 0]} revenu est {clients[0 , 1]} nomber d'achats {clients[0 , 2]} montant depense {clients[0 , 3]}")
print(f"le nomber total est {len(clients)}")
print(f"les dimensions du dataset est {clients.ndim}")
print(clients.shape)

