# Exercici 21: demanar a l'usuari l'entrada de 10 números
# separats per espais. Afegir els nums a una llista
# calcular la suma de tots els números i 
# calcular la mitjana i afegir ambdós a la llista
# mostrar els 10 números estrats, la suma i la mitjana 
entrada = input("Entra 10 nombres separats per espais: ")
lista_nums = entrada.split(' ')
suma = 0
for i in lista_nums:
    num_tmp = int(i)
    suma += num_tmp
mitjana = float(suma/10)
print(f'Números de l\'usuari: {lista_nums[:10]}.')
print(f'Suma total: {suma}.')
print(f'Mitjana: {mitjana}.')