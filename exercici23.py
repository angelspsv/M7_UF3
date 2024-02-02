# Exercici 23: crear una funció per mostrar per la consola
# i desar en un fitxer extern JSON una key anomenada book
# amb atributs titel, cover, year i pages. 
# En el fitxer json haura 4 books amb els seus values
import json

def CrearDesar_json():
    datas = {
        "book": [
            {"title": "Libro1", "cover": "Dura", "year": 2022, "pages": 300},
            {"title": "Libro2", "cover": "Blanda", "year": 2020, "pages": 250},
            {"title": "Libro3", "cover": "Dura", "year": 2021, "pages": 400},
            {"title": "Libro4", "cover": "Blanda", "year": 2019, "pages": 180}
        ]
    }

    print(json.dumps(datas, indent=2))

    # desar el fitxer
    with open("llibres.json", "w") as file:
        json.dump(datas, file, indent=2)

# cridar a la funció
CrearDesar_json()
