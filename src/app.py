import argparse
from models import Bookings, Contacts, Rooms, Users


def actions():
    parser = argparse.ArgumentParser(description="Llamar a las acciones.")
    parser.add_argument(
        "action",
        choices=["read-bookings", "read-rooms", "read-contacts", "read-users", "view-booking"],
        help="La operación que se desea realizar.",
    )

    args = parser.parse_args()

    if args.action == "read-bookings":
        Bookings.list()
    elif args.action == "view-booking":
        Bookings.view()

        
    elif args.action == "read-rooms":
        Rooms.list()
    elif args.action == "read-contacts":
        Contacts.list()
    elif args.action == "read-users":
        Users.list()
    else:
        print("Acción no reconocida.")


actions()
