import argparse
# from models.model_init import Model
from models.bookings import Bookings
from models.rooms import Rooms
from models.contacts import Contacts
from models.users import Users


def actions():
    parser = argparse.ArgumentParser(description="Llamar a las acciones.")
    parser.add_argument(
        "action",
        choices=["read-bookings", 
                 "view-booking",
                 "create-booking",
                 "update-booking",

                 "read-rooms",
                 "view-room",
                 "create-room",
                 "update-room",

                 "read-contacts",
                 "view-contact",
                 "create-contact",
                 "update-contact",

                 "read-users",
                 "view-user", 
                 "create-user",
                 "update-user",
                 ],
        help="La operación que se desea realizar.",
    )

    args = parser.parse_args()

    if args.action == "read-bookings":
        Bookings.list()
    elif args.action == "view-booking":
        Bookings.view()
    elif args.action == "create-booking":
        Bookings.create()
    elif args.action == "update-booking":
        Bookings.update()

    elif args.action == "read-rooms":
        Rooms.list()
    elif args.action == "view-room":
        Rooms.view()
    elif args.action == "create-room":
        Rooms.create()
    elif args.action == "update-room":
        Rooms.update()

    elif args.action == "read-contacts":
        Contacts.list()
    elif args.action == "view-contact":
        Contacts.view()
    elif args.action == "create-contact":
        Contacts.create()
    elif args.action == "update-contact":
        Contacts.update()

    elif args.action == "read-users":
        Users.list()
    elif args.action == "view-user":
        Users.view()
    elif args.action == "create-user":
        Users.create()
    elif args.action == "update-user":
        Users.update()
    else:
        print("Acción no reconocida.")


actions()
