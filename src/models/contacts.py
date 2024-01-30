from models.model_init import Model
from datetime import datetime
from faker import Faker
fake = Faker()

class Contacts(Model):
    path = "../data/contacts.json"

    @classmethod
    def create(cls, type):

        data_contact = {
            "photo": 'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/170.jpg',
            "date": input('Introduzca la fecha YYYY-MM-DD\n') or fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d"),
            "hour": input('Introduzca la hora HH-MM-SS\n') or fake.time(),
            "name": input('Introduzca el nombre\n') or fake.first_name(),
            "last_name": input('Introduzca el apellido\n') or fake.last_name(),
            "email": input('Introduzca el email\n') or fake.email(),
            "telephone": input('Introduzca telefono\n') or fake.phone_number(),
            "archived": bool (input('Esta archivado? true o false\n')) or fake.boolean(),
            "review": input('Introduzca la review\n') or fake.text()
        }
        return Model.create(data_contact, type)

    @classmethod
    def update(cls, type):
        data_contact = Contacts.view(type)
        id = data_contact[0]
        contact = {
            'photo': data_contact[1],
            "date": input(f'Modifique la fecha YYYY-MM-DD: {data_contact[2]}\n') or data_contact[2],
            "hour": input(f'Modifique la hora HH-MM-SS: {data_contact[3]}\n') or data_contact[3],
            "name": input(f'Modifique el nombre: {data_contact[4]}\n') or data_contact[4],
            "last_name": input(f'Modifique el apellido: {data_contact[5]}\n') or data_contact[5],
            "email": input(f'Modifique el email: {data_contact[6]}\n') or data_contact[6],
            "telephone": input(f'Modifique el telefono: {data_contact[7]}\n') or data_contact[7],
            "archived": bool (input(f'Modifique entre true o false): {data_contact[8]}\n')) or data_contact[8],
            "review": input(f'Modifique la review: {data_contact[9]}\n') or data_contact[9]
            }
        return Model.update(contact, type, id)