# Exercici 27: crear una funció que rep 2 números per
# paràmetre i retorna la seva suma.
# Els números es demanen a l'usuari

def Suma(num1, num2):
    print(f'La suma dels dos números és: {num1+num2}.')

def DemanarDosNums():
    num1 = int(input("Entra el primer nombre: "))
    num2 = int(input("Entra el segon nombre: "))
    Suma(num1,num2)
