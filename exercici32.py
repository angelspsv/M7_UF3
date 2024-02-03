# Exercici 32
# crear una funció que agafi 10 nums en una llista i
# retorni una altra llista amb els seus quadrats

def NumerosAlQuadrat():
    num = 0
    llista = []
    llistaQuadrat = []
    while num < 11:
        num = int(input("Entra número: "))
        llista.append(num)
        num+=1
    for i in llista:
        quadrat = i * i
        llistaQuadrat.append(quadrat)
    print(llistaQuadrat)