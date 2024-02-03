# Exercici 28: crear una funció
# rebrà 2 números com paràmetres passats per l'usuari
# retorna un número random entre aquests dos nombres
import random

def ObtenirDosNums():
    num1 = int(input("Entra un número: "))
    num2 = int(input("Entra un altre número: "))
    # el nombre aleatori pot ser un dels dos números que serveixen com a límit
    num_random = random.randint(num1, num2)
    print(f'El número aleatori entre {num1} i {num2} és: {num_random}.')
