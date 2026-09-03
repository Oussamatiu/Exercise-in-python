text1 =  "Transformer des données textuelles et les analyser mots"
text2 = "A partir de 2 textes, transformer chaque texte en liste de mots"

t1 = text1.split(" ")
t2 = text2.split(" ")

ta2 = text1.lower()

ta2 = [ x for x in t1 if len(x) > 3 ]

ta2 = " ".join(ta2).lower()

print(ta2)

word_r = []
for x in t1 :
    for i in t2 :
        if x == i :
            word_r.append(x)

print(word_r)            


# print(t1)
# print(t2)