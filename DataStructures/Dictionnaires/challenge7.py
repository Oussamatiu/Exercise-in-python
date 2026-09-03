etudiants = [
 {"nom": "Omar", "age": 22, "note": 15},
 {"nom": "Sara", "age": 21, "note": 17},
 {"nom": "Yassine", "age": 23, "note": 9},
 {"nom": "Imane", "age": 20, "note": 13},
 {"nom": "Hamza", "age": 24, "note": 7}
]

etu_admis = []
etu_echec = []

for x in etudiants :
    if x["note"] >= 10 :
        etu_admis.append(x)
    else :
        etu_echec.append(x) 
sum = 0          
for x in etudiants :
    sum += x["note"]

max = 0 


for x in etudiants :
    if x["note"] > max :
        max = x["note"]
        name = x["nom"]

print(name)

print(f"la moyenne est : {sum / len(etudiants)}")
         
