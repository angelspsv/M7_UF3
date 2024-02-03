# Exercici 35:
# Crear una funció que rebi una frase per paràmetre
# la frase es demana a l’usuari
# retorna un diccionari amb les paraules 
# i la longitud de cada paraula
def FraseEnDiccionari():
    frase = input("Escriu una frase: ")
    myDict = {}
    myList = frase.split(" ")
    for i in myList:
        myDict[i] = len(i)

    #mostra el diccionari: {'mot': num_lletres}
    print(myDict)

#cridem la funció
FraseEnDiccionari()