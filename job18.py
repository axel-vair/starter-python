#On définit la fonction avec les arguments indéfinis
#On créé une variable qui est égale à une liste des arguments
#On fait un tri de la liste d'arguments stockés dans la variable myList avec la méthond .sort()
#On print la list qui sort triée
#On appelle la fonction avec seulement des chiffres. 
def myInfiniteArgs(*args): 
    myList = [*args]
    myList.sort()
    print(myList)
myInfiniteArgs(1, 3, 4, 2, 6, 9, 8)