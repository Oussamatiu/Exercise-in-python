import numpy as np

notes_metieres = np.array([np.linspace(8 , 20 , num = 5 , endpoint=True , dtype=int ) ,
                           np.linspace(9 , 20 , num = 5 , endpoint=True , dtype=int ),
                            np.linspace(5 , 20 , num = 5 , endpoint=True , dtype=int ),
                             np.linspace(10 , 20 , num = 5 , endpoint=True , dtype=int ),
                              np.linspace(3 , 20 , num = 5 , endpoint=True , dtype=int ),
                               np.linspace(3 , 20 , num = 5 , endpoint=True , dtype=int ) ]) 
matieres = ["math" , "pc" , "ar" , "fr" , "eng"]
etudiants = ["reda" , "ali" , "mohammed" , "morad" , "ahmend" , "moh"]

print(notes_metieres.mean(axis=0))

for x , i in zip(notes_metieres.mean(axis=0) , matieres):
    print( i , x)
    
for x , i , a , z in zip(notes_metieres.mean(axis = 1) ,notes_metieres.max(axis= 1) ,notes_metieres.min(axis= 1) , matieres):

  print(f"pour metiere {z} le moyenne est {x} , la meilleure note est {i} , la faible note est {a} , l'ecart enter elles est {i - a }\n")

for x in etudiants :
    for i in notes_metieres:
        if notes_metieres.mean() < i.mean():
            print(x)
            break

   








