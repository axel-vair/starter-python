import re
#Ouverture du fichier xml et lecture
f = open("data.txt", 'r')
#Tri du fichier
regex = re.findall(r"\b[a-zA-Z]+\b", f.read())
#Nombres de mots triés
print(len(regex))
