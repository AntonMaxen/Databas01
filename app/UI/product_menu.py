from app.UI.menus import menu
import app.BL.product_controller as pc
from app.UI.ui_functions import f_input, print_amount_matches, print_list_of_tablerows, print_tablerow


def get_all_products():
    products = pc.get_all_products()
    print_list_of_tablerows(products)
    print_amount_matches(products)


def get_product_by_id():
    print("Enter a Product Id")
    product = pc.get_product_by_id(f_input())
    print_tablerow(product)


def get_products_by_name():
    print("Enter a Product Name")
    products = pc.get_products_by_name(f_input())
    print_list_of_tablerows(products)
    print_amount_matches(products)


def search_products_menu():
    def inner(column):
        return lambda: get_products_by_columnvalue(column)

    menu({str(i + 1): {"info": c, "func": inner(c)} for i, c in enumerate(pc.get_columns())})


def get_products_by_columnvalue(column_name):
    print(f"Enter searchvalue for {column_name}")
    products = pc.get_products_by_columnvalue(column_name, f_input())
    print_list_of_tablerows(products)
    print_amount_matches(products)


def update_product():
    pass
    print("Enter a product id: ")
    product = pc.get_product_by_id(f_input())

    def inner(column, product):
        return lambda: update_product_column(column, product)

    menu({str(i + 1): {"info": p, "func": inner(p, product)} for i, p in enumerate(pc.get_columns())})


def update_product_column(column, product):
    print("Enter new value: ")
    pc.update_product_column(product, column, f_input())
    print_tablerow(product)


def add_product():
    insert_dict = {}
    for column in pc.get_columns():
        if column != "id":
            insert_dict[column] = input(f'{column}: ')

    pc.add_product(insert_dict)


def delete_product_by_id():
    print("Enter a product id to delete product")
    pc.delete_product(int(f_input()))


def product_menu():
    menu({
        "1": {
            "info": "Show all products",
            "func": get_all_products
        },
        "2": {
            "info": "Get product by id",
            "func": get_product_by_id
        },
        "3": {
            "info": "Get products by name",
            "func": get_products_by_name
        },
        "4": {
            "info": "Filter & Search products by column",
            "func": search_products_menu
        },
        "5": {
            "info": "Update product by ID and column",
            "func": update_product
        },
        "6": {
            "info": "Add a product",
            "func": add_product
        },
        "7": {
            "info": "Delete product",
            "func": delete_product_by_id
        }
    })


if __name__ == '__main__':
    product_menu()
