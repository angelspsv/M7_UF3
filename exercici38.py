# Exercici 38
# cercar errors en el següent codi:

# contactes = {'Roger':678232311, 'Oriol':566879326}
# def elimina(contactes, user):
#   del contactes[user]
#   return contactes[user]
# print(elimina(contactes, 'Pablo'))


# codi corregit
contactes = {'Roger':678232311, 'Oriol':566879326}
def elimina(contactes, user):
    if user in contactes:
        del contactes[user]
        return contactes
    else:
        return "El contacte amb (key) " + user + " no existeix."
    
print(elimina(contactes, 'Pablo'))


# errors:
# la funció elimina() suprimeix un contacte -si existeix al diccionari-, però després vol retornar-ho i això és incorrecte. El return hauria de retornar el diccionari sencer i no un contacte ja suprimit.
# la funció dona error al no existir 'Pablo' dins del diccionari per això s'han d'afegir condicionals: if/else
