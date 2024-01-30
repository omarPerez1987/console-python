from models.model_init import Model
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
        return Model.create(data_room)

    @classmethod
    def update(cls, type):
        data_room = Rooms.view(type)
        id = data_room[0]
        room = {
            'photo': data_room[1],
            "room": input(f'Modifique entre Simple Bed, Double Bed o Suite: {data_room[2]} \n') or data_room[2],
            "bed": input(f'Modifique el numero de Habitación ejemplo P-3: {data_room[3]}\n') or data_room[3],
            "facilities": input(f"Modifique entre Air conditioner, Shop near, Strong Locker, High speed WiFi, Shower, Expert Team: {data_room[4]}\n") or data_room[4],
            "description": input(f'Modifique la descripción\n') or data_room[5],
            "price": int (input(f'Modifique el precio: {data_room[6]}\n') or data_room[6]),
            "discount": int (input(f'Modifique el descuento: {data_room[7]}\n') or data_room[7]),
            "cancel": input(f'Modifique la politica de cancelación: {data_room[8]}\n') or data_room[8],
            "status": input(f'Modifique entre available o booked: {data_room[9]}\n') or data_room[9]
            }
        return Model.update(room, type, id)