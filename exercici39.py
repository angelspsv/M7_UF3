# Exercici 39
# cercar errors en el següent codi d'un triangle de nombres:

# n = int(input("Introdueix l’alçada del triangle (enter positiu): "))
# for i in range(1, n+1, 2):
#   for j in range(j, 1, -1):
#       print(j, end=" ")
#   print("")

# codi corregit

n = int(input("Introdueix l’alçada del triangle (enter positiu): "))
for i in range(1, n+1, 2):
    j = i
    for j in range(j, 0, -2):
        print(j, end=" ")
    print("")


# errors:
# la 'j' havia de ser declarada, no tenia valor
# calia ajustar els valors dins del range() en el for interior