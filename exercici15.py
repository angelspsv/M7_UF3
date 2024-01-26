# Exercici 15: demanar números a l'usuari fins rebre 0
# desar els números dins d'una tupla
# ordenar els números i mostrar la tupla ordenada
num = 2
lista = []
while num != 0:
    num = int(input("Entra un número: "))
    lista.append(num)
lista.pop()
lista.sort()
mi_tupla = tuple(lista)
print(mi_tupla)
    