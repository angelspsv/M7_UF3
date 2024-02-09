# fitxer per crear la taula
import psycopg2
from conn import connection

sql = '''CREATE TABLE IF NOT EXISTS personas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(20),
    apellido VARCHAR(30),
    edad INTEGER,
    email VARCHAR(50),
    movil VARCHAR(15)
);
'''