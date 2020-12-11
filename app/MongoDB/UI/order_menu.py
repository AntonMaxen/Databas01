from app.MongoDB.UI.menus import menu
import app.MongoDB.BL.order_controller as oc
from app.MongoDB.BL.utils import modelobj_to_dict
from app.MongoDB.UI.ui_functions import f_input, print_amount_matches, divider, print_list_of_tablerows, print_tablerow


def get_all_orders():
    orders = oc.get_all_orders()
    print_list_of_tablerows(orders)
    print_amount_matches(orders)


def get_order_by_id():
    print("Enter an order Id")
    o_id = f_input()
    order = oc.get_order_by_id(o_id)
    print_tablerow(order)


def search_orders_menu():
    def inner(column):
        return lambda: get_orders_by_columnvalue(column)

    menu({str(i+1): {"info": o, "func": inner(o)} for i, o in enumerate(oc.get_columns())})


def get_orders_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    orders = oc.get_orders_by_columnvalue(column_name, name)
    print_list_of_tablerows(orders)
    print_amount_matches(orders)


def update_orders():
    print("enter an order id: ")
    o_id = f_input()
    order = oc.get_order_by_id(o_id)

    def inner(column, order):
        return lambda: update_order_column(column, order)

    menu({str(i + 1): {"info": o, "func": inner(o, order)} for i, o in enumerate(oc.get_columns())})


def update_order_column(column, order):
    print("Enter new value: ")
    value = f_input()
    oc.update_order_column(order, column, value)
    print_tablerow(order)


def add_order():
    insert_dict = {}
    for column in oc.get_columns():
        if column != "_id" and column != "id":
            if column == "customer_info":
                value = {}
                value["first_name"] = input('first_name : ')
                value["last_name"] = input('last_name: ')
                value["address"] = input('address: ')
                value["phone"] = input('phone: ')
            elif column == "products":
                running = True
                value = []
                while running:
                    dict_values = {
                        "product_name": input('product_name: '),
                        "retail_price": int(input('retail_price: ')),
                        "storage_location": input('storage_location: '),
                    }
                    value.append(dict_values)
                    print('Do you want to add more products?\n'
                          '1: Yes\n'
                          '2: No')
                    if int(f_input()) == 1:
                        continue
                    else:
                        running = False
            else:
                value = input(f'{column}: ')

            insert_dict[column] = value
    divider()

    order = oc.add_order(insert_dict)
    if order is not None:
        print_tablerow(order)


def drop_order_by_id():
    print("Enter an order id to delete order")
    o_id = f_input()
    oc.drop_order(o_id)


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
            "func": update_orders
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
