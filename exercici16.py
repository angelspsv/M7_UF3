# Exercici 16
# demanar a l'usuari un text
# el programa eliminarà els espais entre mots
# l'afegirà a una tupla i el mostrarà
text = input("Entra un text: ")
lista = [letra for letra in text if letra != ' ']
mi_tupla = tuple(lista)
print(mi_tupla)