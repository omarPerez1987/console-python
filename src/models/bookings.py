from models.model_init import Model
from models.rooms import Rooms
import json
from datetime import datetime
from faker import Faker
fake = Faker()



class Bookings(Model):
    path = "../data/bookings.json"

    @classmethod
    def create(cls, type):
        with open(cls.path) as open_json:
            data = json.load(open_json)
            
        data_booking = {
            "name": input('Introduzca el nombre del cliente\n') or fake.name(),
            "orderDate": datetime.now().strftime("%Y-%m-%d"),
            "orderTime": datetime.now().strftime("%H:%M:%S"),
            "checkin": input(f'Introduzca la fecha de entrada YYYY-MM-DD\n') or fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d"),
            "checkinTime": input('Introduzca la hora de entrada HH:MM:SS\n') or fake.time(),
            "checkout": input('Introduzca la fecha de salida YYYY-MM-DD\n') or fake.date_between(start_date='today', end_date='+1y').strftime("%Y-%m-%d"),
            "checkoutTime": input('Introduzca la hora de salida HH:MM:SS\n') or fake.time(),
            "notes": input('Introduzca la nota\n') or fake.text(),
            "idRoom": int(input(f'Introduzca la habitación asignada entre 1 y {len(data)}\n') or fake.random_int(min=1, max=len(data))),
            "status": input('Eliga la situación del check (checked-in, checked-out o pending)\n') or fake.random_element(elements=('checked-in', 'checked-out', 'pending'))
            }
        return Model.create(data_booking, type)

    @classmethod
    def update(cls, type):

        data_booking = Bookings.view(type)
        id = data_booking[0]
        booking = {
            "name": input(f'\n Modifique el nombre del cliente: {data_booking[1]}\n') or data_booking[1],
            "orderDate": datetime.now().strftime("%Y-%m-%d"),
            "orderTime": datetime.now().strftime("%H:%M:%S"),
            "checkin": input(f'Modifique la fecha de entrada YYYY-MM-DD: {data_booking[4]}\n') or data_booking[4],
            "checkinTime": input(f'Modifique la hora de entrada HH:MM:SS: {data_booking[5]}\n') or data_booking[5],
            "checkout": input(f'Modifique la fecha de salida YYYY-MM-DD: {data_booking[6]}\n') or data_booking[6],
            "checkoutTime": input(f'Modifique la hora de salida HH:MM:SS: {data_booking[7]}\n') or data_booking[7],
            "notes": input(f'Modifique la nota: {data_booking[8]}\n') or data_booking[8],
            "idRoom": int(input(f'Modifique la habitación asignada: {data_booking[9]}\n') or data_booking[9]),
            "status": input(f'Modifique la situación del check (checked-in, checked-out o pending): {data_booking[10]}\n') or data_booking[10]
            }
        return Model.update(booking, type, id)