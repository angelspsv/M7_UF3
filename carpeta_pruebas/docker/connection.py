# en este archivo creare la conexion a la bbdd
import psycopg2

try:
    # datos para la conexion:
    conn = psycopg2.connect(
        database='postgres',
        user='admin',
        password='admin',
        host='localhost',
        port='5432'
    )

    # para hacer la conexion a la base de datos se usa el metodo cursor() 
    # el metodo cursor() crea un objeto para hacer las consultas sql y obtener los resultados
    # el objeto cursor creado esta vinculado a la conexion especifica 
    connection = conn.cursor()

    print("Conexion establecida")
    
    # muestra un objeto cursor
    print(connection)

except psycopg2.Error as e:
    print("No se pudo establecer la conexión.")