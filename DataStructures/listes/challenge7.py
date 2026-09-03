L = [7, 23, 5, 23, 7, 19, 23, 12, 29] 

def compterOccurrences(element , liste):
    n = 0
    for i in liste :
        if i == element:
            n += 1
            

    print(n)

compterOccurrences(23 , L)
