# fitxer Main.py
# des d'aqui es gestionaran les peticions del client
import psycopg2
from psycopg2 import Error
from connection import *
import create
import read
import update
import delete
import create_table


def main():
    # obtenir la connexió des de connection.py
    if not connection:
        print("No es pot establir la connexió a la bbdd")
        return

    try:
        # creació de la taula personas si no existeix
        create_table.create_table_modul()

        # fer les crides de CRUD
        create.create_modul()
        read.read_modul()

        # demanar el nou número de móvil i executar la funció amb la dada
        new_movil_value = input("Entra el nou número de móvil: ")
        update.update_modul(new_movil_value)
        
        # esborrar el darrer registre de la taula
        delete.delete_modul()

    except Error as e:
        print("Error: ", e)
    finally:
        if connection:
            connection.close()
            print("Connexió tancada")

main()