import re
#On stock l'input dans une variable nbr
nbr = int(input("Entrez un nombre : "))
#Ouverture du fichier xml et lecture
f = open("data.txt", 'r')
#Tri du fichier, on rajoute dans le regex la variable nbr que l'on met à l'aide du placeholder %d pour les digits intergrer
regex = re.findall(r"\b[a-zA-Z]{%d}\b" %(nbr), f.read())
#Nombres de mots triés
print(f"Il y a {len(regex)} mots de {nbr} caractères")
 