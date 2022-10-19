#Affichage d'une string
print("Bonjour, quel âge as-tu ?")

#Déclaration de la variable age qui prendra l'input (int pour chiffre) de l'user
age = int(input("Entrez votre âge : "))

#Condition 
if age < 18:
    print("Tu es mineur")
else:
    print("Tu es majeur")
