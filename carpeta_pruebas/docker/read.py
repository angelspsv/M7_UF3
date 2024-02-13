# creamos el archivo read.py para hacer una consulta y devolver los datos de la última entrada
import psycopg2
from connection import *

def read_modul():
    try:





    except psycopg2.Error as error:
        print("Error: ", error)
    
read_modul()