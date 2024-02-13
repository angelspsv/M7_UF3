# el archivo insert.py sirve para hacer entrada de información a la tabla trabajadores
import psycopg2
from connection import *

# creamos el módulo o función que realizará el insert a la tabla trabajadores
def insert_modul():
    try:
        # pedir los datos al usuario: nombre, apellido, nacimiento, email y activo
        nom = input("Entra el nombre: ")
        cognom = input("Entra el apellido: ")
        data_neix = input("Entra la fecha de nacimiento en formato: AAAA/MM/DD: ")
        correu = input("Entra el correo electrónico: ")
        tmp = input("Estado laboral: si o no trabaja: ")
        if tmp == "si" or tmp == "SI":
            actiu = True
        else: 
            actiu = False

        # preparamos la consulta de insert en la tabla
        insert_sql = '''
            INSERT INTO public.trabajadores (nombre, apellido, nacimiento, email, activo) VALUES (%s, %s, %s, %s, %s
        )'''
    
        # datos recogidos del input o entrada y almacenados en values()
        values = (nom, cognom, data_neix, correu, actiu)

        # realizamos el insert a la tabla
        connection.execute(insert_sql, values)

        # guardamos los datos del insert 
        conn.commit()

        print("Entrada de datos realizada con éxito.")

    except psycopg2.Error as error:
        # solamente se verá si se produce un error
        print("Error en la entrada de datos en la tabla de trabajadores.")


