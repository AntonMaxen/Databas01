from app.BL.shops_controller import show_all_shops, show_shop_phone, show_shop_address
from app.UI.menus import menu

shop_menus = {
    "1": show_all_shops,
    "2": show_shop_address,
    "3": show_shop_phone,
}


def shop_menu():
    menu(shop_menus)
