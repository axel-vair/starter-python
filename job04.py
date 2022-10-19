#Valeur input 
valeur = int(input("Entrez un nombre : "))
#On commence avec un compte à -1 pour afficher le 0
count = -1 
#On commence la boucle while, deux paramètres le count qui commence à 0. 
#Tant que la valeur de count est inférieure à la valeur d'utilisateur, alors on incrémente de 1
while (count < valeur):
    count = count + 1 
#On affiche la valeur de count tant que la boucle ne se termine pas
    print('Le compte est :' ,count)
