from models.model_init import Model
import json


class Users(Model):
    path = "../data/users.json"

    @classmethod
    def create(cls):
        with open(cls.path) as open_json:
            data = json.load(open_json)
        data_users = {
            'id': f'{len(data) + 1}',
            'photo': 'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/610.jpg',
            'name': input('Introduzca el nombre\n'),
            'email': input('Introduzca el email\n'),
            'phone': input ('Introduzca el telefono\n'),
            'description': input('Introduzca una descripción\n'),
            'status': input('Eliga inactive o active\n'),
            'startDate': input('Introduzca fecha de alta YYYY/MM/DD\n'),
            'position': input('Eliga Reception, Manager o Service\n'),
            'password': input('Introduzca el password \n')

        }
        print(f'{data_users}')

    @classmethod
    def update(cls):
        data_user = Users.view(id)
        user = {
            'id': data_user["id"],
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
        print(user)
