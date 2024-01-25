from models.model_init import Model
import json
from datetime import datetime



class Bookings(Model):
    path = "../data/bookings.json"

    @classmethod
    def create(cls):
        with open(cls.path) as open_json:
            data = json.load(open_json)
        data_booking = {
            'id': f'{len(data) + 1}',
            "name": input('Introduzca el nombre del cliente\n'),
            "orderDate": datetime.now().strftime("%Y-%m-%d"),
            "orderTime": datetime.now().strftime("%H:%M:%S"),
            "checkin": input('Introduzca la fecha de entrada YYYY-MM-DD\n'),
            "checkinTime": input('Introduzca la hora de entrada HH:MM:SS\n'),
            "checkout": input('Introduzca la fecha de salida YYYY-MM-DD\n'),
            "checkoutTime": input('Introduzca la hora de salida HH:MM:SS\n'),
            "notes": input('Introduzca la nota\n'),
            "idRoom": int (input(f'Introduzca la habitación asignada entre 1 y {len(data)}\n')),
            "check": input('Eliga la situación del check (checked-in, checked-out o pending)\n')

        }
        print(f'{data_booking}')

    @classmethod
    def update(cls):
        data_booking = Bookings.view(id)
        with open(cls.path) as open_json:
            data = json.load(open_json)
        booking = {
            'id': data_booking["id"],
            "name": input(f'Modifique el nombre del cliente: {data_booking["name"]}\n') or {data_booking["name"]},
            "orderDate": datetime.now().strftime("%Y-%m-%d"),
            "orderTime": datetime.now().strftime("%H:%M:%S"),
            "checkin": input(f'Modifique la fecha de entrada YYYY-MM-DD: {data_booking["checkin"]}\n') or {data_booking["checkin"]},
            "checkinTime": input(f'Modifique la hora de entrada HH:MM:SS: {data_booking["checkinTime"]}\n') or {data_booking["checkinTime"]},
            "checkout": input(f'Modifique la fecha de salida YYYY-MM-DD: {data_booking["checkout"]}\n') or {data_booking["checkout"]},
            "checkoutTime": input(f'Modifique la hora de salida HH:MM:SS: {data_booking["checkoutTime"]}\n') or {data_booking["checkoutTime"]},
            "notes": input(f'Modifique la nota: {data_booking["notes"]}\n') or {data_booking["notes"]},
            "idRoom": int (input(f'Modifique la habitación asignada entre 1 y {len(data)}: {data_booking["idRoom"]}\n') or {data_booking["idRoom"]}),
            "check": input(f'Modifique la situación del check (checked-in, checked-out o pending): {data_booking["check"]}\n') or {data_booking["check"]}
            }
        print(booking)