import numpy as np

clients = np.array([[20 , 3000 , 4 , 10000],
                    [30 , 24000, 20 , 50000],
                    [40 , 4000 , 24 , 20000]])

clients_sup_30 = np.where(clients[: , 0] > 30)

print(clients_sup_30)

condition = (clients[: , 0] > 25) & (clients[: , 1] > 5000)

print(clients[condition])
print(len(clients[condition]))