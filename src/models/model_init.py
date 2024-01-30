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
            finally:
                if connection.is_connected():
                    connection.close()
                    print('Conexión cerrada')


    @classmethod
    def create(cls, data):
        print(data)
    
    @classmethod
    def update(cls, data):
        print(data)
    
    @classmethod
    def delete(cls):
        pass

