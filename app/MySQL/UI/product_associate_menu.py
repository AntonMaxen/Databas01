from app.MySQL.UI.menus import menu
import app.MySQL.BL.product_associate_controller as cc
from app.MySQL.UI.ui_functions import f_input, print_amount_matches, divider, print_list_of_tablerows, print_tablerow


def get_all_product_associates():
    product_associates = cc.get_all_product_associates()
    print_list_of_tablerows(product_associates)
    print_amount_matches(product_associates)


def search_product_associates_menu():
    def inner(column):
        return lambda: get_product_associates_by_columnvalue(column)

    menu({str(i+1): {"info": c, "func": inner(c)} for i, c in enumerate(cc.get_columns())})


def get_product_associates_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    product_associates = cc.get_product_associates_by_columnvalue(column_name, name)
    print_list_of_tablerows(product_associates)
    print_amount_matches(product_associates)


def update_product_associate():
    print("enter a id: ")
    c_id = f_input()
    product_associate = cc.get_product_associate_by_id(c_id)

    def inner(column, product_associate):
        return lambda: update_product_associate_column(column, product_associate)

    menu({str(i + 1): {"info": c, "func": inner(c, product_associate)} for i, c in enumerate(cc.get_columns())})


def update_product_associate_column(column, product_associate):
    print("Enter new value: ")
    value = f_input()
    cc.update_product_associate_column(product_associate, column, value)
    print_tablerow(product_associate)


def add_product_associate():
    insert_dict = {}
    for column in cc.get_columns():
        insert_dict[column] = input(f'{column}: ')
    divider()

    product_associate = cc.add_product_associate(insert_dict)


def drop_product_associate_by_id():
    print("Enter a id to delete product_associate")
    c_id = int(f_input())
    cc.drop_product_associate_by_id(c_id)


def product_associate_menu():
    menu({
        "1": {
            "info": "get all product_associates",
            "func": get_all_product_associates
        },
        "2": {
            "info": "search product_associates",
            "func": search_product_associates_menu
        },
        "3": {
            "info": "update a product_associate by id and column",
            "func": update_product_associate
        },
        "4": {
            "info": "add a product_associate",
            "func": add_product_associate
        },
        "5": {
            "info": "drop product_associate by id",
            "func": drop_product_associate_by_id
        }
    })


if __name__ == '__main__':
    product_associate_menu()
