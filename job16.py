#Fonction avec args qui permet de passer de multiples arguments dans la fonction.
def myInfiniteArgs(*args):
    print("J'affiche mes arguments : ", *args)
myInfiniteArgs("Argument1", "Argument2", "Argument3","Argument4","Argument5")
#Appel de la fonction avec les arguments. 