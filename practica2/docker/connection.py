# fitxer per la connexio a la bbdd
import psycopg2

# dades agafades des del fitxer .yml per la connexio a la bbdd
conn = psycopg2.connect(
    database='bbdd',
    user='admin',
    password='admin',
    host='localhost',
    port='5432'
)

# per fer la connexio s'utilitza el metode cursor()
connection = conn.cursor()

print(connection)