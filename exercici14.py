# Exercici 14:
# demanar a l'usuari 10 números separat per un espai
# s'han d'introduir a una tupla i ordenar
# finalment, mostrar la tupla ordenada
numeros = input("Entra 10 números separats per un espai: ")
lista_numeros = [int(num) for num in numeros.split(' ')]
lista_numeros.sort()
mi_tupla = tuple(lista_numeros)
print(mi_tupla)