import argparse
from models import Bookings, Contacts, Rooms, Users


def actions():
    parser = argparse.ArgumentParser(description="Llamar a las acciones.")
    parser.add_argument(
        "action",
        choices=["read-bookings", 
                 "view-booking",

                 "read-rooms",
                 "view-room",

                 "read-contacts",
                 "view-contact",

                 "read-users",
                 "view-user", 
                 ],
        help="La operación que se desea realizar.",
    )

    args = parser.parse_args()

    if args.action == "read-bookings":
        Bookings.list()
    elif args.action == "view-booking":
        Bookings.view()

        
    elif args.action == "read-rooms":
        Rooms.list()
    elif args.action == "view-room":
        Rooms.view()

    elif args.action == "read-contacts":
        Contacts.list()
    elif args.action == "view-contact":
        Contacts.view()

    elif args.action == "read-users":
        Users.list()
    elif args.action == "view-user":
        Users.view()
    else:
        print("Acción no reconocida.")


actions()
