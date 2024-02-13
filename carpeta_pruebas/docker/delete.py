# archivo delete.py que realizará una consulta a la tabla y eliminará la última entrada
import psycopg2
from connection import *

def delete_modul():
    try:
        # preparamos la consulta sql para obtener el último id disponible
        last_id = '''
            SELECT id FROM public.trabajadores ORDER BY id DESC LIMIT 1
        '''

        # ejecuto la consulta sql a la tabla
        connection.execute(last_id)

        # obtengo el id de la última entrada disponible en la tabla
        resultado = connection.fetchone()[0]

        # consulta para eliminar la última entrada disponible
        delete_linia = '''
            DELETE FROM public.trabajadores WHERE id = %s
        '''

        # almaceno la id en una tupla
        values = (resultado,)

        # ejecuto la query
        connection.execute(delete_linia, values)

        # guardamos los cambios realizados en la tabla
        conn.commit()

        print("La última entrada de la tabla ha sido borrada.")

    except psycopg2.Error as error:
        print("Error: ", error)

