# fitxer Main.py
# des d'aqui es gestionaran les peticions del client
import psycopg2
from psycopg2 import Error
from connection import connection
from create.py import create_mod
from read.py import read_mod
from update.py import update_mod
from delete.py import delete_mod


def main():
    # obtenir la connexió des de conn.py
    if not connection:
        print("No es pot establir la connexió a la bbdd")
        return

    try:

        # fer les crides de CRUD
        data = "" #dades a inserir
        create_mod(connection, data)

    except Error as e:
        print("Error: ", e)
    finally:
        if connection:
            connection.close()
            print("Connexió tancada")

main()