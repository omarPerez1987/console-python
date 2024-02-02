from abc import ABC, abstractmethod
from config.mysql import connect
import json


class Model(ABC):
    @abstractmethod
    def __init__(self, path):
        self.path = path

    @classmethod
    def list(cls, type):
        connection = connect()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute(f'SELECT * FROM {type}s')
                res = cursor.fetchall()

                print('Datos de la tabla:')
                for element in res:
                    print(element)
                return res

            except Exception as e:
                print(f'No se pudo mostrar los datos: {e}')

            finally:
                if connection.is_connected():
                    connection.close()
                    print('Conexión cerrada')

    @classmethod
    def view(cls, type):
        id = input(f"Introduzca el id del elemento a buscar...\n")
        connection = connect()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute(f'SELECT * FROM {type}s WHERE id={id}')
                rows = cursor.fetchall()

                if rows:
                    print('Datos de la tabla:')
                for row in rows:
                    print(row)
                    return row
                else:
                    print('Esos datos ya no existen...')

            except Exception as e:
                print(f'No se pudo mostrar los datos: {e}')

            finally:
                if connection.is_connected():
                    connection.close()
                    print('Conexión cerrada')


    @classmethod
    def create(cls, data, type):
        connection = connect()
        if connection:
            try:
                cursor = connection.cursor()

                data['facilities'] = json.dumps(data['facilities'])

                placeholder_list = ['%s'] * len(data)
                placeholders = ', '.join(placeholder_list)

                column_list = list(data.keys())
                columns = ', '.join(column_list)

                values = list(data.values())
                sql = f'INSERT INTO {type}s ({columns}) VALUES ({placeholders})'

                cursor.execute(sql, values)
                connection.commit()

                print('Datos insertados correctamente.')

            except Exception as e:
                print(f'Error al insertar datos: {e}')

            finally:
                if connection.is_connected():
                    connection.close()
                    print('Conexión cerrada')
    
    @classmethod
    def update(cls, data, type, id):
        print(data)

        connection = connect()
        if connection:
            try:
                cursor = connection.cursor()

                placeholder_list = ['%s'] * len(data)
                placeholders = ', '.join(placeholder_list)

                sql = f'UPDATE {type}s SET {placeholders} WHERE id = %s'
                values = list(data.values()) + [id]

                print(cursor.execute(sql, values))
                cursor.execute(sql, values)
                connection.commit()

                print('Datos actualizados correctamente.')

            except Exception as e:
                print(f'Error al actualizar datos: {e}')

            finally:
                if connection.is_connected():
                    connection.close()
                    print('Conexión cerrada')


    
    @classmethod
    def delete(cls, type):
        id = input(f"Introduzca el id del elemento a eliminar...\n")

        connection = connect()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(f'DELETE FROM {type}s WHERE id = {id}')
                connection.commit()              
                print('Datos de la tabla eliminados')

            except Exception as e:
                print(f'Hubo un error al eliminar los datos: {e}')

            finally:
                if connection.is_connected():
                    connection.close()
                    print('Conexión cerrada')


