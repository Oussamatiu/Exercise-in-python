liste =  [1, 2, 3, 4, 5] 
liste2 = [ x**2 for x in liste ]

print(liste2)

liste2.append(30)
print(liste2)

assert len(liste) == len(liste2) , "Attention les 2 listes n'ont pas la même taille"