donnees = ["Omar", 25, "Casablanca", 15.5, True]

for x in donnees :
    print(f"{x} {type(x)}") 
sum_type = {}
string = 0
inti = 0
boole = 0

for x in donnees :
        if isinstance(x , str) :
              string = string + 1
              sum_type["string"] = string 
        if isinstance(x , int) :
              inti = inti + 1
              sum_type["int"] = inti
        if isinstance(x ,bool):
              boole = boole + 1
              sum_type["bool"] = boole      

print(sum_type) 

just_numbers = []

for x in donnees :
    if type(x) is int  or type(x) is float:
          just_numbers.append(x)

print(just_numbers)


