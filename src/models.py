from abc import ABC, abstractmethod


class Model(ABC):
    def __init__(self, path):
        self.path = path

    @classmethod
    def list(cls):
        with open(cls.path) as open_json:
            read_json = open_json.read()
            print(read_json)
    
    @classmethod
    def view(cls):
        pass

    @abstractmethod
    def create(cls):
        pass

    @abstractmethod
    def update(cls):
        pass
    
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
