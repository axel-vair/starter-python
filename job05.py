#Deux valeurs input 
valeur1 = int(input("Entrez la première valeur : "))
valeur2 = int(input("Entrez la deuxième valeur : "))

#Si la valeur1 = valeur 2, on affiche "Valeurs égales"
if (valeur1 == valeur2):
    print("Valeurs égales")
#Si la valeur 1 est supérieure à la valeur 2 alors on affiche la range entre ces deux nombres en incrémentant
elif (valeur1 < valeur2):
    for i in range (valeur1+1,valeur2):
        print(i)
#Si la valeur 1 est inférieure à la valeur 2 alors on affiche la range des deux nombres en décrémentant
elif (valeur1 > valeur2):
    for i in range (valeur1-1,valeur2, -1):
        print(i)

