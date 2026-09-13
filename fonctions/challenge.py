import math

# def number_factorielle() :
#     n = int(input("donner un nomber : "))
#     f = 1
#     for x in range(1 , n + 1):
#         f *= x
#     print(f"la factorielle de ce nombre {n} : {f} ")
   
# number_factorielle()

# def multi_num():
#     m = int(input("donner un nomber : "))
#     for x in range( 1, 11):
#        print(f"{m} * {x} = {m * x}")

# multi_num()      

# def carre_num():
#     L = int(input("donner un nomber : "))
#     racin = math.isqrt(L)
#     if racin * racin == L :
#         print("carré parfai")
#     else :
#         print("pas carre parfai")  

# carre_num()

# def sperate_str():
#     word = input("doneer un mot : ")
#     for x in word:
#         print(x)

# sperate_str()

# def find_long_word():
#     line = input("donner un phrase : ")
#     liste = line.split(" ")
#     long_word = ""
#     maxlen = 0
#     for x in liste:
#         if len(x) > maxlen :
#             long_word = x
#             maxlen = len(x)
#     print(long_word)

# find_long_word()

def num_carater():
    line = input("donner un phrase : ")
    line_without_space = line.replace(" ", "")
    liste_letter = []
    for x in line_without_space :
        if x not in liste_letter:
            liste_letter.append(x)
            num_fois = 0
            for i in line_without_space:
                if x == i :
                    num_fois += 1
            print(f"{x} d’occurrences {num_fois}")
        else:
            continue
      
            

num_carater()

