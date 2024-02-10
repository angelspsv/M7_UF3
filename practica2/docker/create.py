# fitxer per fer un insert a la taula
import psycopg2
from connection import *

def create_modul():
        
    # Consulta SQL para insertar un nuevo registro en la tabla personas
    insert_query = '''
        INSERT INTO public.personas (nombre, apellido, edad, email, movil) VALUES ('Daniel', 'Garcia', 22, 'dani@mail.com', '612345678')
    '''
        
    # Amb el mètode execute() s'envia la query
    connection.execute(insert_query)

    # Commit per fer efectius els canvis de la query a la BD
    conn.commit()
        
    print("Registre creat correctament")

create_modul()