#Initiation des variables qui vont stocker les valeurs inputs
largeur = int(input("Entrez la largeur : "))
hauteur = int(input("Entrez la hauteur : "))

i = 0
#Tant que i inférieur ou égal à la hauteur
while i <= hauteur: 
    if i == 0 or i == hauteur:
        print("|", end="")
        print(largeur * "-", end="")
        print("|")
    
    else:
        print("|", end="")
        print(largeur * " ", end="")
        print("|")
    i+=1 