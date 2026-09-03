def calculer_carre(nomber) :
    
       if not isinstance(nomber,(int , float) ) :
           raise TypeError("Le paramètre doit être un nombre ")
       elif nomber < 0 :
           raise ValueError("Le nombre ne peut pas être négatif")
       return nomber ** 2
for val in [4, "quatre", -2]:
    try:
        print(calculer_carre(val))
    except (TypeError, ValueError) as e:
        print(e)


