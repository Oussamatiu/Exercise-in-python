# name = input("donner voter nom : ")
# email = input("donner voter email : ")
# age = input("donner voter age : ")


# print (name + " " + email + " " + age);



# employe_name = input("donner voter nom : ")
# salaire_horaire = int(input("donner voter salaire horaire : "))
# nomber_heures_t = int(input("donner  le nombre d/'heures travaillées : "))


# if int(nomber_heures_t) > 40 : 
#    plus_h = nomber_heures_t - 40
#    salaire = plus_h * (salaire_horaire * 1.5) + nomber_heures_t * salaire_horaire
# else :
#    salaire = nomber_heures_t * salaire_horaire


# print(salaire);


# age = int(input("donner voter age : "))

# if age < 18 :
#    print("l'entrée est refusée")
# elif age >= 18 & age <= 25 :
#    print("l\'entrée est gratuite")
# else :
#    print("\'entrée est autorisée uniquement si elle est membre du club ou accompagnée d'un membre")



# n = int(input("donnner N : "))
# x = 0

# for i in range(0,n+1):
#     x += i

# print(x);   

# word = input("donner un phrase : ")

# print(word[::-1])

    
#  La suite de Syracuse (aussi appelée suite de Collatz ou conjecture de Syracuse) est une suite définie pour un entier naturel positif n comme suit :

# Si n est pair, le terme suivant est n // 2.

# Si n est impair, le terme suivant est 3n + 1.

# La suite se termine lorsque n devient égal à 1.

# Écrire un code permettant de calculer cette suite


n = int(input("donner un nomber : "))


while n != 1 :
    if n % 2 == 0 :
        n = n // 2
        print(n)
    else:
       n = 3 * n + 1
       print(n)

print(n)
      


   
    
    






