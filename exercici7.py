# Exercici 7: mostrar els nombres imparells de l'1 fins a 500
num = 1
while num < 501:
    result = num%2
    if result == 1:
        print(num)
    num += 1