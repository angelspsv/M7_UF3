# Exercici 9: demanar 2 mots i canviar les dues primeres lletres d'un amb l'altre
mot1 = input("Entra mot 1:")
mot2 = input("Entra mot 2:")
lletres1inici = mot1[0:2]
lletres1fi = mot1[2:]
lletres2inici = mot2[0:2]
lletres2fi = mot2[2:]
motFinal1 = lletres1inici + lletres2fi
motFinal2 = lletres2inici + lletres1fi
print(f'Passem de {mot1} i {mot2} a {motFinal1} i {motFinal2}')