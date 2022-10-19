def mySort(*args): 
    n = len(args)
    argsList = list(args)
    for i in range(n-1):
        for j in range (0, n-1):
            if(argsList[j] > argsList[j+1]):
                argsList[j], argsList[j+1] = argsList[j+1], argsList[j]
    return argsList
    
def myDisplay(argsSort):
    print(argsSort)
myDisplay(mySort(1, 3, 4, 2, 6, 9, 8, 12, 10, 20))


