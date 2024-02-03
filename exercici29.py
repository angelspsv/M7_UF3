# Exercici 29
# crear una funció que rep dos nombres per paràmetre i
# ha de mostrar tots el nombres enters situats entre
# ambdós. També ha de mostrar la suma de tots els nombres
def NumerosEntreDosNums(num1, num2):
    suma = 0
    mi_rango = range(num1, num2)
    for i in mi_rango:
        print(i)
        suma += i
    # així la seqüència inclurà el número d'inici i fi
    print(num2)
    print(f'La suma total de tots el números entre els números és: {suma+num2}.')



def DemanarDosNumeros():
    num1 = int(input("Entra el primer número: "))
    num2 = int(input("Entra el segon número: "))
    if num1 < num2:
        NumerosEntreDosNums(num1, num2)
    elif num1 > num2:
        NumerosEntreDosNums(num2, num1)
    else:
        print("Impossible, els dos números són el mateix")
