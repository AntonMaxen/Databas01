from app.UI.menus import menu
import MySQL.BL.storage_controller as cc
from app.UI.ui_functions import f_input, print_amount_matches, divider, print_list_of_tablerows, print_tablerow


def get_all_storages():
    storages = cc.get_all_storages()
    print_list_of_tablerows(storages)
    print_amount_matches(storages)


def get_storage_by_id():
    print("Enter a Storage Id")
    c_id = f_input()
    storage = cc.get_storage_by_id(c_id)
    print_tablerow(storage)


def search_storages_menu():
    def inner(column):
        return lambda: get_storages_by_columnvalue(column)

    menu({str(i+1): {"info": c, "func": inner(c)} for i, c in enumerate(cc.get_columns())})


def get_storages_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    storages = cc.get_storages_by_columnvalue(column_name, name)
    print_list_of_tablerows(storages)
    print_amount_matches(storages)


def update_storage():
    print("enter a storage id: ")
    c_id = f_input()
    storage = cc.get_storage_by_id(c_id)

    def inner(column, storage):
        return lambda: update_storage_column(column, storage)

    menu({str(i + 1): {"info": c, "func": inner(c, storage)} for i, c in enumerate(cc.get_columns())})


def update_storage_column(column, storage):
    print("Enter new value: ")
    value = f_input()
    cc.update_storage_column(storage, column, value)
    print_tablerow(storage)


def add_storage():
    insert_dict = {}
    for column in cc.get_columns():
        if column != "id":
            insert_dict[column] = input(f'{column}: ')
    divider()

    storage = cc.add_storage(insert_dict)


def drop_storage_by_id():
    print("Enter a storage id to delete storage")
    c_id = int(f_input())
    cc.drop_storage(c_id)


def storage_menu():
    menu({
        "1": {
            "info": "get all storages",
            "func": get_all_storages
        },
        "2": {
            "info": "get storage by id",
            "func": get_storage_by_id
        },
        "3": {
            "info": "search storages",
            "func": search_storages_menu
        },
        "4": {
            "info": "update a storage by id and column",
            "func": update_storage
        },
        "5": {
            "info": "add a storage",
            "func": add_storage
        },
        "6": {
            "info": "drop storage by id",
            "func": drop_storage_by_id
        }
    })


if __name__ == '__main__':
    storage_menu()
