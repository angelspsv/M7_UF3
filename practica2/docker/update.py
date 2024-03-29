# fitxer que actualitza el camp movil de la darrera entrada de la taula personas
import psycopg2
from connection import *

def update_modul(new_movil):

    # consulta SQL per obtenir el ID del darrer registre inserit a la taula personas
    id_query = '''
        SELECT id FROM public.personas ORDER BY id DESC LIMIT 1
    '''
    # execució de la consulta SQL
    connection.execute(id_query)

    # agafem el resultat de la query
    last_id = connection.fetchone()[0]

    # consulta SQL per actualitzar el valor de la columna movil
    update_query = '''
        UPDATE public.personas SET movil = %s WHERE id = %s
    '''
    # dades: l'id del registre que es vol actualitzar i el nou número de móvil
    values = (new_movil, last_id)
        
    # execució de la query per actualitzar el camp movil del darrer registre
    connection.execute(update_query, values)

    # Commit per desar els canvis a la taula/BD
    conn.commit()

    print("Darrer registre actualitzat correctament.")

