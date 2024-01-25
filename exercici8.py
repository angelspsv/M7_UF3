# Exercici 8: demanar a l'usuari l'entrada d'1 a 3 mots
# retornar el/s mot/s, dir quants caràcters té i el 1 i darrer caràcter
entrada = input("Escriu d'u a tres mots:")
mots = entrada.split()
for i in mots:
    print(f'El mot: {i} té: {len(i)} caràcters i el primer càracter és: {i[0]} i el darrer és: {i[-1]}')