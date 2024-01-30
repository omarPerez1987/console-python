from abc import ABC, abstractmethod
from config.mysql import connect
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
                cursor = connection.cursor()
                cursor.execute(f'SELECT * FROM {type}s')
                rows = cursor.fetchall()


                print('Datos de la tabla:')
                for row in rows:
                    print(row)
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
                cursor = connection.cursor()
                cursor.execute(f'SELECT * FROM {type}s WHERE id={id}')
                rows = cursor.fetchall()

                print('Datos de la tabla:')
                for row in rows:
                    print(row)
                    return row
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

                placeholders = ', '.join(['%s'] * len(data))
                columns = ', '.join(data.keys())
                sql = f'INSERT INTO {type}s ({columns}) VALUES ({placeholders})'

                cursor.execute(sql, data)
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

                placeholders = ', '.join([f'{key}=%s' for key in data.keys()])
                sql = f'UPDATE {type}s SET {placeholders} WHERE id = %s'
                values = list(data.values()) + [id]

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
    def delete(cls):
        pass

