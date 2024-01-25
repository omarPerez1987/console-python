from models.model_init import Model
import json


class Rooms(Model):
    path = "../data/rooms.json"

    @classmethod
    def create(cls):
        with open(cls.path) as open_json:
            data = json.load(open_json)
        data_room = {
            'id': f'{len(data) + 1}',
            "photo": "https://picsum.photos/seed/VUK5CD/640/480",
            "room": input('Eliga entre Simple Bed, Double Bed o Suite\n'),
            "bed": input('Escriba el numero de Habitación ejemplo P-3\n'),
            "facilities": input(" Eliga varias Air conditioner, Shop near, Strong Locker, High speed WiFi, Shower, Expert Team\n"),
            "description": input('Introduzca una descripción\n'),
            "price": int(input('Introduzca un precio\n')),
            "discount": int(input('Introduzca un precio\n')),
            "cancel": input('Introduzca politica de cancelación\n'),
            "status": input('Eliga entre available o booked \n')

        }
        print(f'{data_room}')

    @classmethod
    def update(cls):
        data_room = Rooms.view(id)
        room = {
            'id': data_room["id"],
            'photo': data_room["photo"],
            "room": input(f'Modifique entre Simple Bed, Double Bed o Suite: {data_room["room"]} \n') or data_room["room"],
            "bed": input(f'Modifique el numero de Habitación ejemplo P-3: {data_room["bed"]}\n') or {data_room["bed"]},
            "facilities": input(f"Modifique entre Air conditioner, Shop near, Strong Locker, High speed WiFi, Shower, Expert Team: {data_room["facilities"]}\n" or {data_room["facilities"]}),
            "description": input(f'Modifique la descripción\n'),
            "price": int(input(f'Modifique el precio: {data_room["price"]}\n')) or {data_room["price"]},
            "discount": int(input(f'Modifique el descuento: {data_room["discount"]}\n')) or {data_room["discount"]},
            "cancel": input(f'Modifique la politica de cancelación: {data_room["cancel"]}\n') or {data_room["cancel"]},
            "status": input(f'Modifique entre available o booked: {data_room["status"]}\n') or {data_room["status"]}
            }
        print(room)