notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

print(notes)
moyenne = sum(notes) / len(notes)
print(moyenne)
notes_superieur_moyenne = []
for x in notes :
    if x > moyenne :
        notes_superieur_moyenne.append(x)
print(notes_superieur_moyenne)

notes_inferieure_moyenne = []
for x in notes :
    if x < moyenne :
        notes_inferieure_moyenne.append(x)

print(notes_inferieure_moyenne)


print("la meilleure note est : ",max(notes))
print("la mauvaise note est : ",min(notes))

notes_superieur_10 = []
for x in notes :
    if x > 10 :
        notes_superieur_10.append(x)


pourcentage = (len(notes) - len(notes_superieur_10))  / len(notes)  * 100

print("le pourcentage de reussite est : " , int(pourcentage) , "%")



