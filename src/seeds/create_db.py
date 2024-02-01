from config.mysql import connect


connection = connect()
if connection:
    try:
        cursor = connection.cursor()
        with open('src\\seeds\\sql\\database.sql') as sql:
            sql_script = sql.read()

        cursor.execute(sql_script)
        connection.commit()              
        print('Base de datos creada ')

    except Exception as e:
        print(f'Hubo un error al eliminar los datos: {e}')

    finally:
        if connection.is_connected():
            connection.close()
            print('Conexión cerrada')