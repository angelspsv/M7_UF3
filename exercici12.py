# Exercici 12: fer una tupla amb els mesos de l'any
# demanar a l'usuari un número del 0 al 12 i mostrar el mes
# el programa només acaba amb 0
entrada = 2
while entrada != 0:
    tupla_mesos = ("gener", "febrer", "març", "abril", "maig", "juny", "juliol", "agost", "setembre", "octubre", "novembre", "desembre")
    entrada = int(input("Entra el número d'un mes: "))
    if entrada < 1 or entrada > 12:
        if entrada == 0:
            print("Fi del joc")
        else:
            print("Número introduit incorrecte!")
    else:
        print(tupla_mesos[entrada-1])