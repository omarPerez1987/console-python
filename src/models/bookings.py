from models.model import Model
from models.rooms import Rooms
from datetime import datetime
from faker import Faker
fake = Faker()



class Bookings(Model):
    path = "../data/bookings.json"

    @classmethod
    def create(cls, type):
        data_rooms = Rooms.list("room")      
        data_booking = {
            "name": input("Introduzca el nombre del cliente\n") or fake.name(),
            "orderDate": datetime.now().strftime("%Y-%m-%d"),
            "orderTime": datetime.now().strftime("%H:%M:%S"),
            "checkin": input(f"Introduzca la fecha de entrada YYYY-MM-DD\n") or fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),
            "checkinTime": input("Introduzca la hora de entrada HH:MM:SS\n") or fake.time(),
            "checkout": input("Introduzca la fecha de salida YYYY-MM-DD\n") or fake.date_between(start_date="today", end_date="+1y").strftime("%Y-%m-%d"),
            "checkoutTime": input("Introduzca la hora de salida HH:MM:SS\n") or fake.time(),
            "notes": input("Introduzca la nota\n") or fake.text(),
            "idRoom": int(input(f"Introduzca la habitación asignada entre 1 y {len(data_rooms)}\n") or fake.random_int(min=1, max=len(data_rooms))),
            "status": input("Eliga la situación del check (checked-in, checked-out o pending)\n") or fake.random_element(elements=("checked-in", "checked-out", "pending"))
            }
        return Model.create(data_booking, type)

    @classmethod
    def update(cls, type):

        data_booking = Bookings.view(type)
        id = data_booking["id"]
        booking = {
            "name": input(f'Modifique el nombre del cliente: {data_booking["name"]}\n') or data_booking["name"],
            "orderDate": datetime.now().strftime("%Y-%m-%d"),
            "orderTime": datetime.now().strftime("%H:%M:%S"),
            "checkin": input(f'Modifique la fecha de entrada YYYY-MM-DD: {data_booking["checkin"]}\n') or data_booking["checkin"],
            "checkinTime": input(f'Modifique la hora de entrada HH:MM:SS: {data_booking["checkinTime"]}\n') or data_booking["checkinTime"],
            "checkout": input(f'Modifique la fecha de salida YYYY-MM-DD: {data_booking["checkout"]}\n') or data_booking["checkout"],
            "checkoutTime": input(f'Modifique la hora de salida HH:MM:SS: {data_booking["checkoutTime"]}\n') or data_booking["checkoutTime"],
            "notes": input(f'Modifique la nota: {data_booking["notes"]}\n') or {data_booking["notes"]},
            "idRoom": int(input(f'Modifique la habitación asignada: {data_booking["idRoom"]}\n') or data_booking["idRoom"]),
            "status": input(f'Modifique la situación del check (checked-in, checked-out o pending): {data_booking["status"]}\n') or data_booking["status"]
            }
        return Model.update(booking, type, id)