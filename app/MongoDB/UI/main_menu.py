from app.MongoDB.UI.customer_menu import customer_menu
from app.MongoDB.UI.employee_menu import employee_menu
from app.MongoDB.UI.products_menu import product_menu
from app.MongoDB.UI.shop_menu import shop_menu
from app.MongoDB.UI.car_menu import car_menu
from app.MongoDB.UI.order_menu import order_menu
from app.MongoDB.UI.menus import menu

main_menus = {
    "1": {
        "info": "customer menu",
        "func": customer_menu,
    },
    "2": {
        "info": "employee menu",
        "func": employee_menu,
    },
    "3": {
        "info": "shop menu",
        "func": shop_menu,
    },
    "4": {
        "info": "cars menu",
        "func": car_menu
    },
    "5": {
        "info": "orders menu",
        "func": order_menu
    },
    "6": {
        "info": "products menu",
        "func": product_menu
    }
}


def main_menu():
    menu(main_menus)


if __name__ == "__main__":
    main_menu()
