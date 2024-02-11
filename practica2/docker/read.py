# fitxer per fer el READ a la bbdd
import psycopg2
from connection import *

def read_modul():

    # consulta SQL per agafar el darrer insert de la taula personas
    select_query = '''
        SELECT * FROM public.personas ORDER BY id DESC LIMIT 1
    '''

    # s'executeix la consulta SQL
    connection.execute(select_query)

    # el resultat de la consulta SQL
    resultat = connection.fetchall()

    # mostra les dades del darrer insert
    if resultat:
        print("Últim insert a la taula personas:")
        for i in resultat:
            print(i)
    else:
        print("No hi ha registres a la taula personas.")

