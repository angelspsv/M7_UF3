# fitxer per fer un insert a la taula
import psycopg2
from connection import *

def create_modul():

    # demanar les dades de l'usuari des de la consola
    print("Dades de l\'usuari per realitzar una nova entrada a la base de dades: ")
    nom = input("Entra el teu nom: ")
    cognom = input("Entra el teu cognom: ")
    edat = int(input("Entra la teva edat: "))
    email = input("Entra el teu correu: ")
    movil = input("Entra el teu móvil: ")
        
    # Consulta SQL para insertar un nuevo registro en la tabla personas
    insert_query = '''
        INSERT INTO public.personas (nombre, apellido, edad, email, movil) VALUES (%s, %s, %s, %s, %s)
    '''

    # dades agafades per input per la query-insert
    values = (nom, cognom, edat, email, movil)

    # Amb el mètode execute() s'envia la query
    connection.execute(insert_query, values)

    # Commit per fer efectius els canvis de la query a la BD
    conn.commit()
        
    print("Registre creat correctament")
