from app.MySQL.UI.menus import menu
import app.MySQL.BL.product_internal_order_controller as cc
from app.MySQL.UI.ui_functions import f_input, print_amount_matches, divider, print_list_of_tablerows, print_tablerow


def get_all_product_internal_orders():
    product_internal_orders = cc.get_all_product_internal_orders()
    print_list_of_tablerows(product_internal_orders)
    print_amount_matches(product_internal_orders)


def search_product_internal_orders_menu():
    def inner(column):
        return lambda: get_product_internal_orders_by_columnvalue(column)

    menu({str(i+1): {"info": c, "func": inner(c)} for i, c in enumerate(cc.get_columns())})


def get_product_internal_orders_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    product_internal_orders = cc.get_product_internal_orders_by_columnvalue(column_name, name)
    print_list_of_tablerows(product_internal_orders)
    print_amount_matches(product_internal_orders)


def update_product_internal_order():
    print("enter a id: ")
    c_id = f_input()
    product_internal_order = cc.get_product_internal_order_by_id(c_id)

    def inner(column, product_internal_order):
        return lambda: update_product_internal_order_column(column, product_internal_order)

    menu({str(i + 1): {"info": c, "func": inner(c, product_internal_order)} for i, c in enumerate(cc.get_columns())})


def update_product_internal_order_column(column, product_internal_order):
    print("Enter new value: ")
    value = f_input()
    cc.update_product_internal_order_column(product_internal_order, column, value)
    print_tablerow(product_internal_order)


def add_product_internal_order():
    insert_dict = {}
    for column in cc.get_columns():
        insert_dict[column] = input(f'{column}: ')
    divider()

    product_internal_order = cc.add_product_internal_order(insert_dict)


def drop_product_internal_order_by_id():
    print("Enter a id to delete product_internal_order")
    c_id = int(f_input())
    cc.drop_product_internal_order_by_id(c_id)


def product_internal_order_menu():
    menu({
        "1": {
            "info": "get all product_internal_orders",
            "func": get_all_product_internal_orders
        },
        "2": {
            "info": "search product_internal_orders",
            "func": search_product_internal_orders_menu
        },
        "3": {
            "info": "update a product_internal_order by id and column",
            "func": update_product_internal_order
        },
        "4": {
            "info": "add a product_internal_order",
            "func": add_product_internal_order
        },
        "5": {
            "info": "drop product_internal_order by id",
            "func": drop_product_internal_order_by_id
        }
    })


if __name__ == '__main__':
    product_internal_order_menu()
