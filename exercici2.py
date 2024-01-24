#Exercici 2: demanar un nombre a l'usuari
# demanar quin IVA vol aplicar-hi (4, 10 o 21%)
# mostra el nombre introduit, el % de IVA triat i el valor amb IVA
valor = int(input("Entra un valor en euros:"))
iva = int(input("Entra el tipo de IVA: 4, 10 o de 21%:"))
print("El importe introducido por el usuario es:", valor, " y el IVA elegido es: ", iva, " y el importe más IVA es: ", (valor + ((iva*valor)/100)))