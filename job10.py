#Stockage de l'input dans la variable valeur
valeur = input()

#on ouvre un fichier output.txt avec droit d'écriture
#il n'existe pas, donc se créé
#on écrit dans ce fichier, le contenu de la variable et on ferme
file = open("output.txt", "w")
file.write(valeur)
file.close()

#on ouvre le fichier avec droit de lecture
#on affiche le contenu avec la commande read
#on ferme le fichier
file = open("output.txt", "r")
print(file.read())
file.close()
