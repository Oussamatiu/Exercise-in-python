etudiant = {
 "nom": "Omar", "age": 22,
 "formation": {"nom": "Développement IA", "niveau": "Avancé", "duree": 12}
}

print(etudiant["formation"]["nom"])

etudiant["formation"]["niveau"] = "Expert"

print(etudiant)
etudiant["technologies"] = ["Python", "SQL", "Pandas", "MachineLearning"]
print(etudiant)