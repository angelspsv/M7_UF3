# Exercici 17
# demanar a l'usuari un text
# el programa eliminarà els espais entre mots i els caràcters repetirs
# l'afegirà a una tupla i el mostrarà
entrada = input("Entra una frase: ")
lista = [letra for letra in entrada if letra != ' ']
caracteres_unicos = set(lista)
mi_tupla = tuple(caracteres_unicos)
print(mi_tupla)