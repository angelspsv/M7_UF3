# fitxer Main.py
# des d'aqui es gestionaran les peticions del client
import psycopg2
from psycopg2 import Error
from connection import *
import create
import read
import update
import delete


def main():
    # obtenir la connexió des de conn.py
    if not connection:
        print("No es pot establir la connexió a la bbdd")
        return

    try:
        # demanar les dades de l'usuari des de la consola
        print("Dades de l\'usuari per realitzar una nova entrada a la base de dades: ")
        nom = input("Entra el teu nom: ")
        cognom = input("Entra el teu nom: ")
        edat = int(input("Entra la teva edat: "))
        email = input("Entra el teu correu: ")
        movil = input("Entra el teu móvil: ")

        # amb les dades de l'usuari faig un diccionari 
        data = {
            "nombre": nom,
            "apellido": cognom,
            "edad": edat,
            "email": email,
            "movil": movil
        }

        # fer les crides de CRUD
        data = "" #dades a inserir
        create.create_modul(connection, data)
        read.read_modul()
        update.update_modul()
        delete.delete_modul()

    except Error as e:
        print("Error: ", e)
    finally:
        if connection:
            connection.close()
            print("Connexió tancada")

main()