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
        entrada_insert = input("Vols fer una nova entrada de dades? (escriu 'si' en cas afirmatiu): ")
        tmp = entrada_insert.lower()
        if (tmp == 'si'):
            # amb create_modul fem un insert a la taula
            create.create_modul()

        
        entrada_read = input("Vols lleguir la darrera entrada feta a la taula? (escriu 'si' en cas afirmatiu): ")
        tmp1 = entrada_read.lower()
        if (tmp1 == 'si'):
            # amb read_modul lleguim la darrera entrada de la taula personas
            read.read_modul()


        entrada_update = input("Vols actualitzar el valor de la columna 'movil' del darrer usuari? (escriu 'si' en cas afirmatiu): ")
        tmp2 = entrada_update.lower()
        if (tmp2 == 'si'):
            # demanar el nou número de móvil i actualitzem el valor de la columna 'movil'
            new_movil_value = input("Entra el nou número de móvil: ")
            update.update_modul(new_movil_value)


        entrada_delete = input("Vols esborrar la darrera entrada amb dades de la taula? (escriu 'si' en cas afirmatiu): ")
        tmp3 = entrada_delete.lower()
        if (tmp3 == 'si'):
            # esborrar el darrer registre de la taula
            delete.delete_modul()


    except Error as e:
        print("Error: ", e)
    finally:
        if connection:
            connection.close()
            print("Connexió tancada")

# crida del main.py per executar el programa sencer
main()