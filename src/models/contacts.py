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
        id = data_contact['id']
        contact = {
            'photo': data_contact["photo"],
            "date": input(f'Modifique la fecha YYYY-MM-DD: {data_contact["date"]}\n') or data_contact["date"],
            "hour": input(f'Modifique la hora HH-MM-SS: {data_contact["hour"]}\n') or data_contact["hour"],
            "name": input(f'Modifique el nombre: {data_contact["name"]}\n') or data_contact["name"],
            "last_name": input(f'Modifique el apellido: {data_contact["last_name"]}\n') or data_contact["last_name"],
            "email": input(f'Modifique el email: {data_contact["email"]}\n') or data_contact["email"],
            "telephone": input(f'Modifique el telefono: {data_contact["telephone"]}\n') or data_contact["telephone"],
            "archived": bool (input(f'Modifique entre true o false): {data_contact["archived"]}\n')) or data_contact["archived"],
            "review": input(f'Modifique la review: {data_contact["review"]}\n') or data_contact["review"]
            }
        return Model.update(contact, type, id)