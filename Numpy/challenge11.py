import numpy as np

temperatures = np.array([22, 23, 21, 24, 22, 25, 23, 80, 24, 22,-10])

moyenne = temperatures.mean()
ecate = np.std(temperatures)



normales = temperatures[
    (temperatures >= moyenne - 2 * ecate) &
    (temperatures <= moyenne + 2 * ecate)
]

suspecte = temperatures[
    (temperatures < moyenne - 2 * ecate) |
    (temperatures > moyenne + 2 * ecate)
    ]


where_normales = np.where( 
    (temperatures >= moyenne - 2 * ecate) &
    (temperatures <= moyenne + 2 * ecate))[0] + 1
where_suspecte = np.where(
    (temperatures < moyenne - 2 * ecate) |
    (temperatures > moyenne + 2 * ecate))[0] + 1

number_normales = len(normales)
number_suspecte = len(suspecte)

print(f"les valeurs normales : {normales}")
print(f"les valeurs suspectes : {suspecte}")

print(f"les position des normales : {where_normales}")
print(f"les position des suspectes : {where_suspecte}")

print(f"les nomber des normales est {number_normales} ")
print(f"les nomber des suspectes est {number_suspecte} ")


