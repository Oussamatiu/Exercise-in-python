import numpy as np


temperatures = np.array([30 , 28 , 32, 41 , 26])

moyenne_temp = temperatures.mean()

jour_chauds = np.argmax(temperatures)

jour_froids = np.argmin(temperatures)


print(f"jour  plus chauds {jour_chauds + 1} temperature est {temperatures[jour_chauds]}")
print(f"jour  plus froids {jour_froids + 1} temperature est {temperatures[jour_froids]}")


print(f"l'amplitude thermique est {np.max(temperatures) - np.min(temperatures)}")



temp_sup_moyenne = temperatures[temperatures > moyenne_temp]

print(f"les temperatures superieures a la moyenne : {temp_sup_moyenne}")

variation = np.diff(temperatures)

print(variation)

