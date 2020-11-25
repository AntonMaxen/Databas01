from app.UI.menus import menu
import app.BL.order_product_controller as cc
from app.UI.ui_functions import f_input, print_amount_matches, divider, print_list_of_tablerows, print_tablerow


def get_all_order_products():
    order_products = cc.get_all_order_products()
    print_list_of_tablerows(order_products)
    print_amount_matches(order_products)


def search_order_products_menu():
    def inner(column):
        return lambda: get_order_products_by_columnvalue(column)

    menu({str(i+1): {"info": c, "func": inner(c)} for i, c in enumerate(cc.get_columns())})


def get_order_products_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    order_products = cc.get_order_products_by_columnvalue(column_name, name)
    print_list_of_tablerows(order_products)
    print_amount_matches(order_products)


def update_order_product():
    print("enter a id: ")
    c_id = f_input()
    order_product = cc.get_order_product_by_id(c_id)

    def inner(column, order_product):
        return lambda: update_order_product_column(column, order_product)

    menu({str(i + 1): {"info": c, "func": inner(c, order_product)} for i, c in enumerate(cc.get_columns())})


def update_order_product_column(column, order_product):
    print("Enter new value: ")
    value = f_input()
    cc.update_order_product_column(order_product, column, value)
    print_tablerow(order_product)


def add_order_product():
    insert_dict = {}
    for column in cc.get_columns():
        if column != "id":
            insert_dict[column] = input(f'{column}: ')
    divider()

    order_product = cc.add_order_product(insert_dict)


def drop_order_product_by_id():
    print("Enter a id to delete order_product")
    c_id = int(f_input())
    cc.drop_order_product_by_id(c_id)


def order_product_menu():
    menu({
        "1": {
            "info": "get all order_products",
            "func": get_all_order_products
        },
        "2": {
            "info": "search order_products",
            "func": search_order_products_menu
        },
        "3": {
            "info": "update a order_product by id and column",
            "func": update_order_product
        },
        "4": {
            "info": "add a order_product",
            "func": add_order_product
        },
        "5": {
            "info": "drop order_product by id",
            "func": drop_order_product_by_id
        }
    })


if __name__ == '__main__':
    order_product_menu()
