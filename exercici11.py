# Exercici 11
# Demanar a l'usuari un número entre 10 i 100 i amb aquest
# fer un tupla de l'1 fins aquest número. Mostrar la tupla
entrada = int(input("Entra un número entre 10 i 100: "))
if entrada <= 100 and entrada >= 10:
    tmp = range(1, entrada+1)
    miTupla = tuple(tmp)
    print(miTupla)
else:
    print("Número introduit està fora del rang")