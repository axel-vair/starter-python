#Déclaration de la variable valeur qui stocke l'input
valeur = input(">")


#Tant que différent de au revoir alors on reste dans la boucle 
while valeur != "Au revoir":
#Si valeur == bonjour alors on affiche "bonjour à toi"
    if(valeur == "Bonjour"):
        print("Bonjour à toi")
#Si la valeur est égale à Au revoir alors il quitte.
    elif(valeur == "Au revoir"):
        exit()    
    valeur = input(">")