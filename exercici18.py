# Exercici 18: demanar 2 mots a l'usuari
# introduir els mots a una tupla
# dir quantes vegades apareix cada lletra
entrada = input("Entra dos mots: ")
lista_letras = [letra for letra in entrada if letra != ' ']
lista_letras_unicas = set(lista_letras)
for letra in lista_letras_unicas:
    contador = entrada.count(letra)
    print(f'De la lletra {letra} hi ha {contador} cops.')