#Création d'une fonction avec args indéfinis
#initiation d'une variable qui est égale aux args
#Boucle for qui permet le stockage dans my list des paramètres
#Si le modulo 2 = 0 alors on affiche x. 
def myInfiniteArgs(*args): 
    myList = args

    for x in myList:
        if x % 2 == 0:
            print(x)
    
myInfiniteArgs(1, 2, 3, 4, 5)
