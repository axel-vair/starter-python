#On définit une fonction
#on déclare une variable dans laquelle on stock la len de args
#on déclare une variable argList dans laquelle on stocker args que l'on transforme en liste
#on passe par une boucle for -1
#on neest une boucle for  on donne un start à 0 et on arrête à n-1
#Si j est supérieur à j+1 alors on swap 
def myInfiniteArgs(*args): 
    n = len(args)
    argsList = list(args)
    for i in range(n-1):
        for j in range (0, n-1):
            if(argsList[j] > argsList[j+1]):
                argsList[j], argsList[j+1] = argsList[j+1], argsList[j]
    print(argsList)
myInfiniteArgs(1, 3, 4, 2, 6, 9, 8, 12, 10, 20)

