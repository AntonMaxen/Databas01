from app.UI.menus import menu
import MySQL.BL.shop_storage_controller as cc
from app.UI.ui_functions import f_input, print_amount_matches, divider, print_list_of_tablerows, print_tablerow


def get_all_shop_storages():
    shop_storages = cc.get_all_shop_storages()
    print_list_of_tablerows(shop_storages)
    print_amount_matches(shop_storages)


def search_shop_storages_menu():
    def inner(column):
        return lambda: get_shop_storages_by_columnvalue(column)

    menu({str(i+1): {"info": c, "func": inner(c)} for i, c in enumerate(cc.get_columns())})


def get_shop_storages_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    shop_storages = cc.get_shop_storages_by_columnvalue(column_name, name)
    print_list_of_tablerows(shop_storages)
    print_amount_matches(shop_storages)


def update_shop_storage():
    print("enter a id: ")
    c_id = f_input()
    shop_storage = cc.get_shop_storage_by_id(c_id)

    def inner(column, shop_storage):
        return lambda: update_shop_storage_column(column, shop_storage)

    menu({str(i + 1): {"info": c, "func": inner(c, shop_storage)} for i, c in enumerate(cc.get_columns())})


def update_shop_storage_column(column, shop_storage):
    print("Enter new value: ")
    value = f_input()
    cc.update_shop_storage_column(shop_storage, column, value)
    print_tablerow(shop_storage)


def add_shop_storage():
    insert_dict = {}
    for column in cc.get_columns():
        insert_dict[column] = input(f'{column}: ')
    divider()

    shop_storage = cc.add_shop_storage(insert_dict)


def drop_shop_storage_by_id():
    print("Enter a id to delete shop_storage")
    c_id = int(f_input())
    cc.drop_shop_storage_by_id(c_id)


def shop_storage_menu():
    menu({
        "1": {
            "info": "get all shop_storages",
            "func": get_all_shop_storages
        },
        "2": {
            "info": "search shop_storages",
            "func": search_shop_storages_menu
        },
        "3": {
            "info": "update a shop_storage by id and column",
            "func": update_shop_storage
        },
        "4": {
            "info": "add a shop_storage",
            "func": add_shop_storage
        },
        "5": {
            "info": "drop shop_storage by id",
            "func": drop_shop_storage_by_id
        }
    })


if __name__ == '__main__':
    shop_storage_menu()
