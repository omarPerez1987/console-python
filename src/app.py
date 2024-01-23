import argparse
from models import Bookings, Contacts, Rooms, Users


input_action = input('Que quieres listar? read-bookings, read-rooms, read-contacts o read-users')

def actions(action):
    parser = argparse.ArgumentParser(description="Llamar a las acciones.")
    parser.add_argument(
        "action",
        # choices=["read-bookings", "read-rooms", "read-contacts", "read-users"],
        choices=[action],
        help="La operación que se desea realizar.",
    )

    args = parser.parse_args()

    if args.action == "read-bookings":
        Bookings(Bookings.path).list()
    elif args.action == "read-rooms":
        Rooms(Rooms.path).list()
    elif args.action == "read-contacts":
        Contacts(Contacts.path).list()
    elif args.action == "read-users":
        Users(Users.path).list()
    else:
        print("Acción no reconocida.")

actions(input_action)
