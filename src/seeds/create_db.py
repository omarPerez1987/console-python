from config.connect_db import connect
import os

path_dir = os.path.dirname(os.path.abspath(__file__))
sql_path = os.path.join(path_dir, 'sql', 'database.sql')



connection = connect()
if connection:
    try:
        cursor = connection.cursor()
        with open(sql_path) as sql:
            sql_script = sql.read()

        cursor.execute(sql_path)

        connection.commit()              
        print('Base de datos creada y tablas con datos insertados')

    except Exception as e:
        print(f'Hubo un error al crear la base de datos: {e}')

    finally:
        if connection.is_connected():
            connection.close()
            print('Conexión cerrada')
