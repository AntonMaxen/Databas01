from app.UI.customer_menu import customer_menu
from app.UI.menu_shops import shop_menu
from app.UI.menus import menu

main_menus = {
    "1": {
        "info": "customer menu",
        "func": customer_menu,
    },
    "2": {
        "info": "shop menu",
        "func": shop_menu
    }
}


def main_menu():
    menu(main_menus)


if __name__ == "__main__":
    main_menu()
