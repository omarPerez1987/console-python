from abc import ABC, abstractmethod
import json


class Model(ABC):
    @abstractmethod
    def __init__(self, path):
        self.path = path

    @classmethod
    def list(cls):
        with open(cls.path) as open_json:
            read_json = open_json.read()
            print(read_json)

    @classmethod
    def view(cls):
        with open(cls.path) as open_json:
            data = json.load(open_json)
            print(f"Introduzca el id del elemento del 1 al {len(data)}")
            id = input()

            if int(id) > int(len(data)) or int(id) < 1:
                print(f"El id introducido ({id}) no está entre 1 y {len(data)}")
            else:
                for element in data:
                    if element["id"] == int(id):
                        print(element)
                        return element

    

    @classmethod
    def delete(cls):
        pass

