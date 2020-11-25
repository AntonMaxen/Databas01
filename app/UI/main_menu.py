from app.UI.customer_menu import customer_menu
from app.UI.menu_shops import shop_menu
from app.UI.car_menu import car_menu
from app.UI.customer_car_menu import customer_car_menu
from app.UI.employee_menu import employee_menu
from app.UI.order_menu import order_menu
from app.UI.order_product_menu import order_product_menu
from app.UI.storage_menu import storage_menu
from app.UI.shop_storage_menu import shop_storage_menu
from app.UI.product_associate_menu import product_associate_menu
from app.UI.car_model_menu import car_model_menu
from app.UI.compatibilty_menu import compatibility_menu
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
    },
    "6": {
        "info": "order menu",
        "func": order_menu
    },
    "7": {
        "info": "order has products menu",
        "func": order_product_menu
    },
    "8": {
        "info": "storage menu",
        "func": storage_menu
    },
    "9": {
        "info": "shop storage menu",
        "func": shop_storage_menu
    },
    "10": {
        "info": "product associates menu",
        "func": product_associate_menu
    },
    "11": {
        "info": "car model menu",
        "func": car_model_menu
    },
    "12": {
        "info": "compatibility menu",
        "func": compatibility_menu
    }

}


def main_menu():
    menu(main_menus)


if __name__ == "__main__":
    main_menu()
