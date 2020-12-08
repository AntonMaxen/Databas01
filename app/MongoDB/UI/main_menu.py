from app.MongoDB.UI.customer_menu import customer_menu
from app.MongoDB.UI.menus import menu

main_menus = {
    "1": {
        "info": "customer menu",
        "func": customer_menu,
    },
}


def main_menu():
    menu(main_menus)


if __name__ == "__main__":
    main_menu()
