from app.MySQL.UI.menus import menu
import app.MySQL.BL.order_controller as cc
from app.MySQL.UI.ui_functions import f_input, print_amount_matches, divider, print_list_of_tablerows, print_tablerow


def get_all_orders():
    orders = cc.get_all_orders()
    print_list_of_tablerows(orders)
    print_amount_matches(orders)


def get_order_by_id():
    print("Enter a Order Id")
    c_id = f_input()
    order = cc.get_order_by_id(c_id)
    print_tablerow(order)


def get_orders_by_name():
    print("Enter a Order Name")
    c_name = f_input()
    orders = cc.get_orders_by_name(c_name)
    print_list_of_tablerows(orders)
    print_amount_matches(orders)


def search_orders_menu():
    def inner(column):
        return lambda: get_orders_by_columnvalue(column)

    menu({str(i+1): {"info": c, "func": inner(c)} for i, c in enumerate(cc.get_columns())})


def get_orders_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    orders = cc.get_orders_by_name(column_name, name)
    print_list_of_tablerows(orders)
    print_amount_matches(orders)


def update_order():
    print("enter a order id: ")
    c_id = f_input()
    order = cc.get_order_by_id(c_id)

    def inner(column, order):
        return lambda: update_order_column(column, order)

    menu({str(i + 1): {"info": c, "func": inner(c, order)} for i, c in enumerate(cc.get_columns())})


def update_order_column(column, order):
    print("Enter new value: ")
    value = f_input()
    cc.update_order_column(order, column, value)
    print_tablerow(order)


def add_order():
    insert_dict = {}
    for column in cc.get_columns():
        if column != "id":
            insert_dict[column] = input(f'{column}: ')
    divider()

    order = cc.add_order(insert_dict)


def drop_order_by_id():
    print("Enter a order id to delete order")
    c_id = int(f_input())
    cc.drop_order(c_id)


def order_menu():
    menu({
        "1": {
            "info": "get all orders",
            "func": get_all_orders
        },
        "2": {
            "info": "get order by id",
            "func": get_order_by_id
        },
        "3": {
            "info": "search orders",
            "func": search_orders_menu
        },
        "4": {
            "info": "update a order by id and column",
            "func": update_order
        },
        "5": {
            "info": "add a order",
            "func": add_order
        },
        "6": {
            "info": "drop order by id",
            "func": drop_order_by_id
        }
    })


if __name__ == '__main__':
    order_menu()
