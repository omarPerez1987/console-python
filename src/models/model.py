from abc import ABC, abstractmethod
from config.connect_db import connect
import json


class Model(ABC):
    @abstractmethod
    def __init__(self, path):
        self.path = path

    @classmethod
    def list(cls, type):
        print(type)
        connection = connect()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute(f'SELECT * FROM {type}s')
                res = cursor.fetchall()

                print('Datos de la tabla:')
                for element in res:
                    for key, value in element.items():
                        print(f"{key}: {value}")
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
                res = cursor.fetchall()

                if res:
                    print('Datos de la tabla:')
                for element in res:
                    for key, value in element.items():
                        print(f"{key}: {value}")
                    return element
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
        connection = connect()
        if connection:
            try:
                cursor = connection.cursor()

                update_values = ', '.join([f"{column} = %s" for column in data.keys()])

                sql = f'UPDATE {type}s SET {update_values} WHERE id = %s'

                values = list(data.values()) + [id]

                
                print(data)
                cursor.execute(sql, values)
                # connection.commit()
                print('***********************************')
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
                # connection.commit()              
                print('Datos de la tabla eliminados')

            except Exception as e:
                print(f'Hubo un error al eliminar los datos: {e}')

            finally:
                if connection.is_connected():
                    connection.close()
                    print('Conexión cerrada')


