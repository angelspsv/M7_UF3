# fitxer per crear la taula
import psycopg2
from connection import *

def create_table_modul():
    # per fer la connexio s'utilitza el metode cursor()

    sql = '''CREATE TABLE IF NOT EXISTS personas (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(20),
        apellido VARCHAR(30),
        edad INTEGER,
        email VARCHAR(50),
        movil VARCHAR(15)
    )
    '''

    # Amb el mètode execute() s'envia la query
    connection.execute(sql)

    # Commit per fer efectius els canvis de la query a la BD
    conn.commit()

    print("Taula creada")
