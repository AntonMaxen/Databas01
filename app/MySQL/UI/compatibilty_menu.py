from app.UI.menus import menu
import MySQL.BL.compatibility_controller as cc
from app.UI.ui_functions import f_input, print_amount_matches, divider, print_list_of_tablerows, print_tablerow


def get_all_compatibilitys():
    compatibilitys = cc.get_all_compatibilitys()
    print_list_of_tablerows(compatibilitys)
    print_amount_matches(compatibilitys)


def get_compatibility_by_id():
    print("Enter a Compatibility Id")
    c_id = f_input()
    compatibility = cc.get_compatibility_by_id(c_id)
    print_tablerow(compatibility)


def search_compatibilitys_menu():
    def inner(column):
        return lambda: get_compatibilitys_by_columnvalue(column)

    menu({str(i+1): {"info": c, "func": inner(c)} for i, c in enumerate(cc.get_columns())})


def get_compatibilitys_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    compatibilitys = cc.get_compatibilitys_by_columnvalue(column_name, name)
    print_list_of_tablerows(compatibilitys)
    print_amount_matches(compatibilitys)


def update_compatibility():
    print("enter a compatibility id: ")
    c_id = f_input()
    compatibility = cc.get_compatibility_by_id(c_id)

    def inner(column, compatibility):
        return lambda: update_compatibility_column(column, compatibility)

    menu({str(i + 1): {"info": c, "func": inner(c, compatibility)} for i, c in enumerate(cc.get_columns())})


def update_compatibility_column(column, compatibility):
    print("Enter new value: ")
    value = f_input()
    cc.update_compatibility_column(compatibility, column, value)
    print_tablerow(compatibility)


def add_compatibility():
    insert_dict = {}
    for column in cc.get_columns():
        insert_dict[column] = input(f'{column}: ')
    divider()

    compatibility = cc.add_compatibility(insert_dict)


def drop_compatibility_by_id():
    print("Enter a compatibility id to delete compatibility")
    c_id = int(f_input())
    cc.drop_compatibility(c_id)


def compatibility_menu():
    menu({
        "1": {
            "info": "get all compatibilitys",
            "func": get_all_compatibilitys
        },
        "2": {
            "info": "get compatibility by id",
            "func": get_compatibility_by_id
        },
        "3": {
            "info": "search compatibilitys",
            "func": search_compatibilitys_menu
        },
        "4": {
            "info": "update a compatibility by id and column",
            "func": update_compatibility
        },
        "5": {
            "info": "add a compatibility",
            "func": add_compatibility
        },
        "6": {
            "info": "drop compatibility by id",
            "func": drop_compatibility_by_id
        }
    })


if __name__ == '__main__':
    compatibility_menu()
