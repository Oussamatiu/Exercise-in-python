import numpy as np

from challenge4 import clients


clients[0][1] = 1000 



clients[: , 0] = clients[0 , :]

clients1 = clients[0 , :].copy()

print(clients1)

clients1[0] = 0

print(clients1)
print(clients)




