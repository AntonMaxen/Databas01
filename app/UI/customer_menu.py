from app.UI.menus import menu
from app.BL.place_holder import main

customer_menus = {
    "1": main
}


def customer_menu():
    menu(customer_menus)


if __name__ == '__main__':
    customer_menu()
