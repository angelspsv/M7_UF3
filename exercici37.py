# Exercici 37
# Cercar errors en el següent programa:

# ftotal = input('Introdueix el preu de tot el carrito: ')
# print(amb_iva(ftotal, iva))
# def amb_iva(ftotal, iva = 21):
# ftotal = ftotal * iva
# return ftotal

def amb_iva(ftotal, iva):
    total = ((ftotal * iva)/100) + ftotal
    return total

ftotal = int(input('Introdueix el preu de tot el carrito: '))
print(amb_iva(ftotal, 21))




# errors:
# el valor de l'input s'ha de convertir a int()
# la funció amb_iva() es vol servir abans de ser definida
# quan es crida la funció amb_iva no s'assigna valor a iva
# en la definició de la funció amb_iva, iva pot ser una variable, pero no es pot definir així el seu valor
# el càlcul total amb iva no és correcte, el correcte és: total = ((ftotal * iva)/100) + ftotal