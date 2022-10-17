#stockage de l'input dans la variable valeur 
valeur = int(input())
#boucle for qui range entre 1 et la valeur de l'input +1
for i in range(1, valeur + 1):
#on multiplie l'espace par valeur entrée - i, on ajoute le slash
    print(" " * (valeur - i), "/", end="")
    print(" " * 2 * (i - 1), "\\", sep="")
print("/" + "_" * 2 * valeur + "\\")
# On termine avec les derniers slashs puis les tirets que l'on multiplie par deux fois la valeur pour la base
