# Exercici 24:
# crear una funció per llegir el contingut del fitxer extern
# creat a l'exercici 23 i mostrar-ho tot per la consola
# en format json
import json

def ReadFile():
# Així es mostra tot el contingut del fitxer 
    with open("llibres.json", 'r') as file:
        result = json.load(file)
#       print(result)   així ho mostra tot en una línia
        print(json.dumps(result, indent=2))

ReadFile()