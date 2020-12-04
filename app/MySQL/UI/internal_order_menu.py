from app.MySQL.UI.menus import menu
import datetime
import app.MySQL.BL.internal_order_controller as cc
from app.MySQL.UI.ui_functions import f_input, print_amount_matches, divider, print_list_of_tablerows, print_tablerow


def get_all_internal_orders():
    internal_orders = cc.get_all_internal_orders()
    print_list_of_tablerows(internal_orders)
    print_amount_matches(internal_orders)


def get_internal_order_by_id():
    print("Enter a InternalOrder Id")
    c_id = f_input()
    internal_order = cc.get_internal_order_by_id(c_id)
    print_tablerow(internal_order)


def search_internal_orders_menu():
    def inner(column):
        return lambda: get_internal_orders_by_columnvalue(column)

    menu({str(i+1): {"info": c, "func": inner(c)} for i, c in enumerate(cc.get_columns())})


def get_internal_orders_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    internal_orders = cc.get_internal_orders_by_columnvalue(column_name, name)
    print_list_of_tablerows(internal_orders)
    print_amount_matches(internal_orders)


def update_internal_order():
    print("enter a internal_order id: ")
    c_id = f_input()
    internal_order = cc.get_internal_order_by_id(c_id)

    def inner(column, internal_order):
        return lambda: update_internal_order_column(column, internal_order)

    menu({str(i + 1): {"info": c, "func": inner(c, internal_order)} for i, c in enumerate(cc.get_columns())})


def update_internal_order_column(column, internal_order):
    print("Enter new value: ")
    value = f_input()
    cc.update_internal_order_column(internal_order, column, value)
    print_tablerow(internal_order)


def add_internal_order():
    insert_dict = {}
    for column in cc.get_columns():
        if column != "id":
            if column == "lead_time":
                insert_dict[column] = datetime.datetime.now()
            else:
                insert_dict[column] = input(f'{column}: ')
    divider()

    internal_order = cc.add_internal_order(insert_dict)


def drop_internal_order_by_id():
    print("Enter a internal_order id to delete internal_order")
    c_id = int(f_input())
    cc.drop_internal_order(c_id)


def internal_order_menu():
    menu({
        "1": {
            "info": "get all internal_orders",
            "func": get_all_internal_orders
        },
        "2": {
            "info": "get internal_order by id",
            "func": get_internal_order_by_id
        },
        "3": {
            "info": "search internal_orders",
            "func": search_internal_orders_menu
        },
        "4": {
            "info": "update a internal_order by id and column",
            "func": update_internal_order
        },
        "5": {
            "info": "add a internal_order",
            "func": add_internal_order
        },
        "6": {
            "info": "drop internal_order by id",
            "func": drop_internal_order_by_id
        }
    })


if __name__ == '__main__':
    internal_order_menu()
