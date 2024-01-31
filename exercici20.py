# Exercici 20: crear un diccionari (key:value)
# la clau serà el nom i el valor serà l'edat
# si la clau / nom es repeteix no s'afegirà al diccionari
# indicant-ho. S'acaba l'entrada de nous usuaris
# quan l'usuari ho indiqués 
myDict = {}
desig = "si"
while desig == "si":
    desig = input("Vols entrar un nou contacte? Escriu \'no\' per acabar...")
    tmp = desig.lower()
    desig = tmp
    if desig == "si":
        nom = input("Entra el nom: ")
        if nom in myDict:
            print("Aqust nom ja existeix!")
        else:
            edat = int(input("Entra l'edad: "))
            myDict[nom] = edat
            years = myDict[nom]
            print(f'La nova entrada és: {nom}:{years}')