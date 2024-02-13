# archivo update.py para modificar el valor de email del último trabajador de la tabla
import psycopg2
from connection import *

def update_modul():
    try:
        new_mail = input("Entra el nuevo correo: ")
        # hago la consulta sql para conocer el id del último usuario disponible en la tabla
        id_consulta = '''
            SELECT id FROM public.trabajadores ORDER BY id DESC LIMIT 1
        '''

        # ejecuto la consulta para conocer el id
        connection.execute(id_consulta)

        # el último id es:
        respuesta_id = connection.fetchone()[0]

        # ahora hago la consulta para actualizar el correo del último usuario
        update_query = '''
            UPDATE public.trabajadores SET email = %s WHERE id = %s
        '''

        # los datos para la consulta: el nuevo email y la id del trabajador X
        values = (new_mail, respuesta_id)

        # ejecutamos la query y actualizamos el correo
        connection.execute(update_query, values)

        # guardamos los cambios realizados en la tabla
        conn.commit()

        print("El valor de la columna email se ha actualizado correctamente.")

    except psycopg2.Error as error:
        print("Error: ", error)

