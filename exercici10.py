# Exercici 10: cal endevinar un número entre 1-100
# l'usuari introdueix números fins endevinar i rep 
# si és més petit o gran que el endevinable
# missatge de l'acert i el nombre d'intents
entrada = 0
intents = 0
while entrada != 22:
    entrada = int(input("Endevina el número entre 1-100:"))
    intents += 1
    if entrada < 1 or entrada > 100:
        print("El número ha de ser entre 1 i 100:")
    else:
        if entrada == 22:
            print(f'Has guanyat! Intents: {intents}')
        elif entrada < 22:
            print(f'El número introduit {entrada} és menor')
        else:
            print(f'El número introduit {entrada} és mayor')