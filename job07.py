#Range de 1 à 100
for i in range (1,101): 
#On déclare une variable j qui est égale à la valeur i 
    j = i
#Si i modulo trois = zéro ET modulo cinq = zéro alors j = FizzBuzz
    if(i % 3 == 0 and i % 5 == 0):
        j = "FizzBuzz"
#Même chose si i modulo trois = zéro
    elif(i % 3 == 0):
        j = "Fizz"
#Même chose si i modulo cinq
    elif(i % 5 == 0):
        j = "Buzz"
 
#On affiche j
    print(j)
    
    