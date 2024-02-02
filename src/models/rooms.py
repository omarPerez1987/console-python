from models.model import Model
import json
from faker import Faker
fake = Faker()


class Rooms(Model):
    path = "../data/rooms.json"

    @classmethod
    def create(cls, type):
        data_room = {
            "photo": "https://picsum.photos/seed/VUK5CD/640/480",
            "room": input('Elige entre Simple Bed, Double Bed o Suite\n') or fake.random_element(elements=('Simple Bed', 'Double Bed', 'Suite')),
            "bed": input('Escribe el número de Habitación, por ejemplo P-3\n') or f'{fake.random_letter()}-{fake.random_int(min=1, max=9)}',
            "facilities": fake.random_elements(elements=('Air conditioner', 'Shop near', 'Strong Locker', 'High speed WiFi', 'Shower', 'Expert Team'), length=3),
            "description": input('Introduce una descripción\n') or fake.text(),
            "price": int(input('Introduce un precio\n') or fake.random_int(min=50, max=300)),
            "discount": int(input('Introduce un descuento\n') or fake.random_int(min=0, max=50)),
            "cancel": input('Introduce la política de cancelación\n') or fake.sentence(),
            "status": input('Elige entre "available" o "booked"\n') or fake.random_element(elements=('available', 'booked'))
        }
        return Model.create(data_room, type)

    @classmethod
    def update(cls, type):
        data_room = Rooms.view(type)
        id = data_room['id']
        room = {
            'photo': data_room["photo"],
            "room": input(f'Modifique entre Simple Bed, Double Bed o Suite: {data_room["room"]} \n') or data_room["room"],
            "bed": input(f'Modifique el numero de Habitación ejemplo P-3: {data_room["bed"]}\n') or data_room["bed"],
            "facilities": input(f"Modifique entre Air conditioner, Shop near, Strong Locker, High speed WiFi, Shower, Expert Team: {data_room["facilities"]}\n" or {data_room["facilities"]}),
            "description": input(f'Modifique la descripción\n'),
            "price": int (input(f'Modifique el precio: {data_room["price"]}\n') or data_room["price"]),
            "discount": int (input(f'Modifique el descuento: {data_room["discount"]}\n') or data_room["discount"]),
            "cancel": input(f'Modifique la politica de cancelación: {data_room["cancel"]}\n') or data_room["cancel"],
            "status": input(f'Modifique entre available o booked: {data_room["status"]}\n') or data_room["status"]
            }
        return Model.update(room, type, id)