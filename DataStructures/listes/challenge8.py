L = [7, 23, 5, 23, 7, 19, 23, 12, 29, 7, 5]

for x in L :
    n = 0
    for a in L :
        if x == a :
            n += 1
    
    print(f"{x} -> {n}")    

