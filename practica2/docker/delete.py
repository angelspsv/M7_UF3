# fitxer delete.py que elimina el darrer registre a la taula personas
import psycopg2
from connection import *

def delete_modul():
    #consulta query per esbrinar quin és el darrer id disponible a la taula
    id_query = '''
        SELECT id FROM public.personas ORDER BY id DESC LIMIT 1
    '''

    # execució de la consulta SQL 
    connection.execute(id_query)

    # resultat de la consulta sql
    last_id = connection.fetchone()[0]

    # Consulta SQL per eliminar el últim registre de la taula
    delete_query = '''
        DELETE FROM public.personas WHERE id = %s
    '''

    value = (last_id,)

    # execució de la consulta SQL per esborrar la darrera entrada de la taula
    connection.execute(delete_query, value)

    # commit per desar els canvis a la taula/base de dades
    conn.commit()

    print("Últim registre esborrat correctament.")
