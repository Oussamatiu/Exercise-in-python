langages = ["Python", "Java", "JavaScript", "C++"]

langages.append("PHP")
print(langages)
langages.append("SQL")
langages.insert(1 , "C")

langages.remove("Java")

print(langages)

langages.pop()
print(langages , len(langages))