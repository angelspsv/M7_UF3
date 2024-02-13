# la funció del fitxer crear_taula és crear la taula trabajador si no existeix
# tendrà los siguientes columnas: id, nombre, apellido, fecha de nacimiento, email, activo
import psycopg2
from connection import *


try:
    # el mòdul demanarà les dades a l'usuari per la consola
    def crear_taula_modul():
        # consulta sql
        sql_create_table = '''CREATE TABLE IF NOT EXISTS trabajadores(
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(20) NOT NULL,
            apellido VARCHAR(30) NOT NULL,
            nacimiento DATE NOT NULL,
            email VARCHAR(50) NOT NULL,
            activo BOOLEAN
        )'''

        # con el método execute() se realiza la orden sql de crear la tabla
        connection.execute(sql_create_table)

        # con el método commit() se guardan los cambios realizados en la bbdd por la query
        conn.commit()

        print("Tabla realizada con éxito.")


except (Exception, psycopg2.Error) as error:
    # mensaje de error si sale alguno durante el proceso de creación
    print("Error al crear la tabla de trabakadores: ", error)

