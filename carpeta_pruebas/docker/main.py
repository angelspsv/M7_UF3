# archivo main.py donde se ejecutará todas las operaciones CRUD: insert, read, update y delete
import psycopg2
import crear_taula_trabajador
from connection import *

def main_modul():
    #comprobamos la conexión
    if not connection:
        print("No se puede conectar a la bbdd.")
        return
    
    try:
        # creación de la tabla
        crear_taula_trabajador.crear_taula_modul()

        # hacemos un insert a la tabla


    except psycopg2.Error as e:
        print("Error: ", e)
    
    finally:
        if connection:
            # cerrar el cursor
            connection.close()
            # cerrar la conexión a la bbdd
            conn.close()
            print("Conexión cerrada.")


# cridem la funció 
main()