from app.UI.customer_menu import customer_menu
from app.UI.menu_shops import shop_menu
from app.UI.car_menu import car_menu
from app.UI.customer_car_menu import customer_car_menu
from app.UI.employee_menu import employee_menu
from app.UI.menus import menu

main_menus = {
    "1": {
        "info": "customer menu",
        "func": customer_menu,
    },
    "2": {
        "info": "shop menu",
        "func": shop_menu
    },
    "3": {
        "info": "car menu",
        "func": car_menu
    },
    "4": {
        "info": "customer car menu",
        "func": customer_car_menu
    },
    "5": {
        "info": "employee menu",
        "func": employee_menu
    }
}


def main_menu():
    menu(main_menus)


if __name__ == "__main__":
    main_menu()
