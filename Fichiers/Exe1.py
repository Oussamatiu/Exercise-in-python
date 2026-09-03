with open('data/exercice.txt' , 'r') as fichier :
    text = fichier.readlines()
    dicts = {}
    for x in text :
        for i in ["[INFO]", "[WARNING]", "[ERROR]", "[DEBUG]", "[CRITICAL]"]:
            if i in x:
                if i not in dicts.keys():
                    dicts[i] = []
                dicts[i].append(x.replace(i, "").strip())
print(dicts)
dicts2 = {}
with open('data/resume_logs.txt' , 'w') as fichier :
    for x in dicts :
       dicts2[x] = len(dicts[x])
        
    fichier.write(str(dicts2)) 
