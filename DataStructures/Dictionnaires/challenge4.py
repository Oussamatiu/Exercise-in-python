notes_etudiants = {"Omar": 15, "Sara": 8, "Yassine": 17, "Imane": 11, "Hamza": 6, "Nadia":
14}

etudiants_reussie = {}
etudiants_ech = {}

for x , i in notes_etudiants.items() :
    if i >= 10 :
        etudiants_reussie[x] = i
    else :
        etudiants_ech[x] = i

pourcentage = (len(etudiants_reussie) - len(etudiants_ech)) *  100  / len(notes_etudiants)

print(f"pourcentage est {pourcentage}%")

meilleur = max(etudiants_reussie, key=etudiants_reussie.get)

     

print(f"e meilleur étudiant est {meilleur}")



