from app.UI.menus import menu
import app.BL.product_controller as pc
import app.UI.ui_utils as ui
import app.BL.utils as utils


def get_all_products():
    p = pc.get_all_products()
    for product in utils.modelobj_to_dict(p):
        ui.print_dict(product)
        ui.divider()


def get_product_by_id():
    print("Enter a product ID: ")
    product_obj, product_dict = pc.get_product_by_id(ui.f_input())
    ui.print_dict(product_dict)
    ui.divider()
    ## TODO : Build query that joins associates and with product by ID and list there
    print("Suppliers & Manufacturers:")
    print("1) Associate - Attributes - ETC")
    print("2) Bssociate - Attributes - ETC")
    print("3) Csso.. build models to fetch associates... ")
    ui.divider()


def get_products_by_name():
    print("Enter a Product Name")
    p_name = ui.f_input()
    products = pc.get_products_by_name(p_name)
    for product in products:
        ui.print_dict(product)
        ui.divider()

    ui.print_amount_matches(products)


def search_products_menu():
    def inner(column):
        return lambda: get_products_by_columnvalue(column)

    menu({str(i + 1): {"info": c, "func": inner(c)} for i, c in enumerate(pc.get_columns())})


def get_products_by_columnvalue(column_name):
    print(f"enter search value for {column_name}")
    name = ui.f_input()
    products = pc.get_products_by_columnvalue(column_name, name)
    for products in products:
        ui.print_dict(products)
        ui.divider()

    ui.print_amount_matches(products)


def update_product():
    print("enter a product id: ")
    p_id = ui.f_input()
    product_obj, product_dict = pc.get_product_by_id(p_id)

    def inner(column, product_obj):
        return lambda: update_product_column(column, product_obj, product_dict)

    menu({str(i + 1): {"info": c, "func": inner(c, product_obj)} for i, c in enumerate(pc.get_columns())})


def update_product_column(column, product_obj, product_dict):
    print("Enter new value: ")
    value = ui.f_input()
    pc.update_product_column(product_obj, column, value)
    ui.print_dict(product_dict)
    ui.divider()


def add_product():
    insert_dict = {}
    for column in pc.get_columns():
        if column != "id":
            insert_dict[column] = input(f'{column}: ')

    pc.add_product(insert_dict)


def delete_product_by_id():
    print("Enter a product id to delete product")
    p_id = int(ui.f_input())
    pc.delete_product(p_id)


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
