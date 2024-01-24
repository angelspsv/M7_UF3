#Exercici 5, demanar un nombre i dir si és parell o senar
num = int(input("Entra un número:"))
resultat = num % 2
if resultat == 0:
    print("El número introducido es par")
else:
    print("El número introducido es impar")