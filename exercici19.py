# Exercici 19:
# s'ha dde mostra una serie de dades extretes d'una llista
# cal fer servir el ':' 
# 1) Imprimir el segon element
# 2) Imprimir l’últim element
# 3) Imprimir l’àrea de la terrassa
# 4) Imprimir del primer element al tercer element
# 5) Imprimir del tercer element a l’últim
# 6) Imprimir el total de l'àrea de les dues habitacions
# 7) Modificar l’àrea del lavabo i imprimir la nova list area
# 8) Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
# 9) Imprimir el total de l’àrea del pis.

areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

# Entenc per 1r element el elemente de la posició 0
print(f'El segon element és: {areas_pis[1:2]}.')
longitud = len(areas_pis)
print(f'L\'ultim element de la llista és: {areas_pis[(longitud-1):]}.')
print(f'Mostrar l\'area de la terrassa: {areas_pis[7:8]}.')
print(f'Mostrar del 1r al 3r elements: {areas_pis[:3]}.')
print(f'Imprimir del 3r element fins al final: {areas_pis[2:]}.')
hab1 = float(areas_pis[5:6][0])
hab2 = float(areas_pis[(longitud-1):][0])
total_habs = hab1 + hab2
print(f'Mostrar el total de l\'area de les dues habitacions: {total_habs}.')
areas_pis[9] = 10
print(f'El nou àrea del bany és: {areas_pis[9:10]}.')
areas_pis.append("Pati_interior")
areas_pis.append(2.78)
print(f'Imprimir la nova list area: {areas_pis[:]}.')
menj = float(areas_pis[1:2][0])
rebe = float(areas_pis[3:4][0])
terr = float(areas_pis[7:8][0])
bany = float(areas_pis[9:10][0])
cuin = float(areas_pis[11:12][0])
total = total_habs + menj + rebe + terr + bany + cuin
print(f'Total area del pis: {total}.')
