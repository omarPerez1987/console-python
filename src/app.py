import argparse
from models.bookings import Bookings
from models.rooms import Rooms
from models.contacts import Contacts
from models.users import Users

options_action = {"1": "list", "2": "view", "3": "create", "4": "update"}
options_type = {"1": "booking", "2": "room", "3": "contact", "4": "user"}

action_mapping = {
    "list": {"booking": Bookings.list, "room": Rooms.list, "contact": Contacts.list, "user": Users.list},
    "view": {"booking": Bookings.view, "room": Rooms.view, "contact": Contacts.view, "user": Users.view},
    "create": {"booking": Bookings.create, "room": Rooms.create, "contact": Contacts.create, "user": Users.create},
    "update": {"booking": Bookings.update, "room": Rooms.update, "contact": Contacts.update, "user": Users.update},
}

action_number = input(f"Que quieres hacer? {', '.join(f'{key}:{value}' for key, value in options_action.items())}: ")
action = options_action.get(action_number)


type_number = input(f"Donde quieres {action}: {', '.join(f'{key}:{value}' for key, value in options_type.items())}: ")
type = options_type.get(type_number)

def actions():
    if action and type in action_mapping[action]:
        action_mapping[action][type]()
    else:
        print("Acción no reconocida.")

actions()
