# creamos el archivo read.py para hacer una consulta y devolver los datos de la última entrada
import psycopg2
from connection import *

def read_modul():
    try:
        # la consulta cogerá la última entrada de la tabla basándose en el id que es
        # autoincremental y después mostrará el resultado por la consola
        select_sql = '''
            SELECT * FROM public.trabajadores ORDER BY id DESC LIMIT 1
        '''

        # ejecutamos la consulta sql para conocer la última entrada en la tabla
        connection.execute(select_sql)

        # trabajamos con el resultado de la query
        resultado = connection.fetchall()

        # para visualizar los datos devueltos del select/consulta sql
        if resultado:
            print("El último resultado que figura en la tabla es: ")
            for i in resultado:
                print(i)
        else:
            print("No hay resultados en la tabla.")

    except psycopg2.Error as error:
        print("Error: ", error)
    