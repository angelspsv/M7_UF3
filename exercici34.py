# Exercici 34:
# Crear una funció que rep per paràmetres una funció i una llista
# Ha de crear una nova llista amb els valors nous i mostrar-la
# Crear una funció que calculi el quadrat d’un número passat per paràmetre
llista_nums = [1, 2, 5, 7, 10]

# funció que rep una funció i una llista i retorna/mostra una nova llista
def FuncioQueRepFuncioiLlista(funcio, llista):
    nova_llista = [funcio(i) for i in llista]
    print(nova_llista)

# multiplica al quadrat el número rebut i el retorna
def AlQuadrat(num):
    return num * num

# cridem la funció
FuncioQueRepFuncioiLlista(AlQuadrat, llista_nums)