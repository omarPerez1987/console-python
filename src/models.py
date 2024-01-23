from abc import ABC, abstractmethod
import json


class Model(ABC):
    def __init__(self, path):
        self.path = path

    @classmethod
    def list(cls):
        with open(cls.path) as open_json:
            read_json = open_json.read()
            print(read_json)

    @classmethod
    @classmethod
    def view(cls):
        with open(cls.path) as open_json:
         data = json.load(open_json)
         print("Enter id of element")
         find_id = input()
         
        for i in data:
            if i["id"] == int(find_id):
                print(i)

    # @abstractmethod
    # def create(cls):
    #     pass

    # @abstractmethod
    # def update(cls):
    #     pass

    @classmethod
    def delete(cls):
        pass


class Bookings(Model):
    path = "../data/bookings.json"


class Contacts(Model):
    path = "../data/contacts.json"


class Rooms(Model):
    path = "../data/rooms.json"


class Users(Model):
    path = "../data/users.json"
