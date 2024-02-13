# archivo main.py donde se ejecutará todas las operaciones CRUD: insert, read, update y delete
import psycopg2
import crear_taula_trabajador
from connection import *
import insert
import read
import update
import delete

def main_modul():
    #comprobamos la conexión
    if not connection:
        print("No se puede conectar a la bbdd.")
        return
    
    try:
        # creación de la tabla
        crear_taula_trabajador.crear_taula_modul()

        # hacemos un insert a la tabla
        insert.insert_modul()

        # consultamos la última entrada en la tabla
        read.read_modul()
        
        # modificaremos el valor de la columna email
        update.update_modul()

        # eliminar la última entrada disponible en la tabla 
        delete.delete_modul()


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
main_modul()