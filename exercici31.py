# Exercici 31
# Crear una funció per calcular el IVA d’un import
# La funció rep per paràmetre la quantitat sense IVA i l’IVA a aplicar (introduïts per l’usuari)
# valors d'IVA possibles: 4, 10 i 21%
# si el valor d'IVA is empty o diferent als possibles s'aplicarà el 21
# Es mostrarà per pantalla el valor sense IVA, l’IVA i el total.

def CalcularPreuAmbIVA():
    iva = 0
    tmp = input("Entra el \'%\' d'IVA a aplicar al preu: ")
    preu_sense_iva = int(input("Entra el preu sense IVA: "))
    if tmp == "":
        iva = 21
    else:
        tmp2 = int(tmp)
        if tmp2 == 4 or tmp2 == 10:
            iva = tmp2
        else:
            iva = 21
    preu_amb_iva = ((preu_sense_iva * iva) / 100) + preu_sense_iva
    print(f'El preu del producte sense IVA: {preu_sense_iva}, amb l\'IVA de {iva} aplicat és: {preu_amb_iva}.')
