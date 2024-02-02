from models.bookings import Bookings
from models.rooms import Rooms
from models.contacts import Contacts
from models.users import Users
import subprocess
import os

action_mapping = {
    "list": {"booking": Bookings.list, "room": Rooms.list, "contact": Contacts.list, "user": Users.list},
    "view": {"booking": Bookings.view, "room": Rooms.view, "contact": Contacts.view, "user": Users.view},
    "create": {"booking": Bookings.create, "room": Rooms.create, "contact": Contacts.create, "user": Users.create},
    "update": {"booking": Bookings.update, "room": Rooms.update, "contact": Contacts.update, "user": Users.update},
    "delete": {"booking": Bookings.delete, "room": Rooms.delete, "contact": Contacts.delete, "user": Users.delete},
}

options_action = {"1": "list", "2": "view", "3": "create", "4": "update", "5": "delete"}
options_type = {"1": "booking", "2": "room", "3": "contact", "4": "user"}


def validate(options, len): 
    if options > 0 and options <= len:
        return True
    else:
        print("Opción no reconocida.\n")
        actions()

def actions():

        action_text = []
        for key, value in options_action.items():
            action_text.append(f'{key}: {value}')

        action_number= int(input(f"Elige una opción:\n{'    '.join(action_text)}\n"))
        
        validate(action_number, len(options_action))
        if validate:
            action = options_action.get(str(action_number))
        

        type_text = []
        for key, value in options_type.items():
            type_text.append(f'{key}: {value}')

        type_number= int(input(f"Elige una opción:\n{'    '.join(type_text)}\n"))

        validate(type_number, len(options_type))
        if validate:
            type = options_type.get(str(type_number))  

        if action and type in action_mapping[action]:
            action_mapping[action][type](type)
        else:
            print("Acción no reconocida.")


def run_create_db():
    input('Creando base de datos. Presiona Enter para continuar...')
    subprocess.run(['python', 'seeds/create_db.py'], shell=True)

def run_actions():
    actions()

if __name__ == "__main__":
    print('Bienvenido admin.\n')

    response_create_db = input('¿Ya tienes una base de datos llena? (si/no)\n')
    if response_create_db.lower() == 'no':
        run_create_db()

    run_actions()


