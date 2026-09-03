notes = {"Python": 15, "SQL": 13, "JavaScript": 17, "Git": 14, "Linux": 12}


print(notes.keys())
print(notes.values())
print(notes.items())
print(sum(notes.values())/ len(notes))
print(f"la meilleur est {max(notes.values())} \nla mauvaise note est {min(notes.values())}")