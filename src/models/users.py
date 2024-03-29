from models.model import Model
import json
from faker import Faker
fake = Faker()


class Users(Model):
    path = "../data/users.json"

    @classmethod
    def create(cls, type):
        data_users = {
            'photo': 'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/610.jpg',
            'name': input('Introduzca el nombre\n') or fake.name(),
            'email': input('Introduzca el email\n') or fake.email(),
            'phone': input('Introduzca el telefono\n') or fake.phone_number(),
            'description': input('Introduzca una descripción\n') or fake.text(),
            'status': input('Eliga inactive o active\n') or fake.random_element(elements=('inactive', 'active')),
            'startDate': input('Introduzca fecha de alta YYYY/MM/DD\n') or fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d"),
            'position': input('Eliga Reception, Manager o Service\n') or fake.random_element(elements=('Reception', 'Manager', 'Service')),
            'password': input('Introduzca el password\n') or fake.password()
        }
        return Model.create(data_users, type)

    @classmethod
    def update(cls, type):
        data_user = Users.view(type)
        id = data_user['id']
        user = {
            'photo': data_user["photo"],
            'name': input(f'Modifique el nombre: {data_user["name"]}\n') or data_user["name"],
            'email': input(f'Modifique el email: {data_user["email"]}\n') or data_user["email"],
            'phone': input (f'Modifique el phone: {data_user["phone"]}\n') or data_user["phone"],
            'description': input(f'Modifique la descripción: {data_user["description"]}\n') or data_user["description"],
            'status': input(f'Modifique entre inactive o active: {data_user["status"]}\n') or data_user["status"],
            'startDate': input(f'Modifique la fecha de alta YYYY/MM/DD: {data_user["startDate"]}\n') or data_user["startDate"],
            'position': input(f'Modifique entre Reception, Manager o Service: {data_user["position"]}\n') or data_user["position"],
            'password': input(f'Modifique el password: {data_user["password"]} \n') or data_user["password"]
            }
        return Model.update(user, type, id)
