from models.bookings import Bookings
from models.rooms import Rooms
from models.contacts import Contacts
from models.users import Users

action_mapping = {
    "list": {"booking": Bookings.list, "room": Rooms.list, "contact": Contacts.list, "user": Users.list},
    "view": {"booking": Bookings.view, "room": Rooms.view, "contact": Contacts.view, "user": Users.view},
    "create": {"booking": Bookings.create, "room": Rooms.create, "contact": Contacts.create, "user": Users.create},
    "update": {"booking": Bookings.update, "room": Rooms.update, "contact": Contacts.update, "user": Users.update},
}

options_action = {"1": "list", "2": "view", "3": "create", "4": "update"}
options_type = {"1": "booking", "2": "room", "3": "contact", "4": "user"}

def validate(options): 
    if options > 0 and options < 5:
        return True
    else:
        print("Opción no reconocida.\n")
        actions()


def actions():
    action_number = input(f"Elige una opción:\n{''.join(f'{key}: {value}   ' for key, value in options_action.items())}\n")
    action_number = int(action_number)
    validate(action_number)
    if validate:
        action = options_action.get(str(action_number))
    

    type_number = input(f"Elige una opción:\n{''.join(f'{key}: {value}   ' for key, value in options_type.items())}\n")
    type_number = int(type_number)

    validate(type_number)
    if validate:
        type = options_type.get(str(type_number))  

    if action and type in action_mapping[action]:
        action_mapping[action][type]()
    else:
        print("Acción no reconocida.")

actions()
