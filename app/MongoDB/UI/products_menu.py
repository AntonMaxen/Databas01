from app.MongoDB.UI.menus import menu
import app.MongoDB.BL.product_controller as pc
import app.MongoDB.BL.associate_controller as ac
import app.MongoDB.BL.shop_controller as sc
from app.MongoDB.UI.ui_functions import f_input, print_amount_matches, divider, print_list_of_tablerows, print_tablerow


def product_format(product):
    print(f'ID: {product._id}')
    print(f'Name: {product.product_name}')
    print(f'Purchase Price: {product.purchase_price}')
    print(f'Retail Price: {product.retail_price}')
    for si in product.storage_info:
        shop = sc.get_shop_by_id(si['shop_id'])
        print(f'StorageInfo: {shop._id} | Store: {shop.address_line_one} @ {shop.city} | Stock: {si["product_amount"]}')
    associate = ac.get_associate_by_id(product.associate[0])
    print(f'Associate: {product.associate[0]} | {associate.name} | Role: {associate.associates_category} | email {associate.associates_category}')
    divider()
    
def get_all_products():
    products = pc.get_all_products()
    for p in products:
        product_format(p)
    print_amount_matches(products)

#  5fd0bc15323105f9caf8de2a
def get_product_by_id():
    print("Enter a Product Id")
    p_id = f_input()
    product = pc.get_product_by_id(p_id)
    product_format(product)
    divider()


def get_product_by_name():
    print("Enter a Product Name")
    p_name = f_input()
    products = pc.get_products_by_name(p_name)
    print_list_of_tablerows(products)
    print_amount_matches(products)


def search_products_menu():
    def inner(column):
        return lambda: get_products_by_columnvalue(column)

    menu({str(i+1): {"info": p, "func": inner(p)} for i, p in enumerate(pc.get_columns())})


def get_products_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    products = pc.get_products_by_columnvalue(column_name, name)
    print_list_of_tablerows(products)
    print_amount_matches(products)


def update_product():
    print("enter a product id: ")
    p_id = f_input()
    product = pc.get_product_by_id(p_id)

    def inner(column, product):
        return lambda: update_product_column(column, product)

    menu({str(i + 1): {"info": p, "func": inner(p, product)} for i, p in enumerate(pc.get_columns())})


def update_product_column(column, product):
    print("Enter new value: ")
    value = f_input()
    pc.update_product_column(product, column, value)
    print_tablerow(product)


def add_product():
    insert_dict = {}
    for column in pc.get_columns():
        if column != "_id" and column != "id":
            # hook up associates
            # hook up storage info
            # empty orders []
            input(f'{column}: ')


def delete_product_by_id():
    print("Enter a product id to delete product")
    p_id = f_input()
    deleted = pc.delete_product(p_id)
    if deleted:
        print(f'Product {p_id} was successfully deleted')
    divider()


def product_menu():
    menu({
        "1": {
            "info": "get all products",
            "func": get_all_products
        },
        "2": {
            "info": "get product by id",
            "func": get_product_by_id
        },
        "3": {
            "info": "get product by name",
            "func": get_product_by_name
        },
        "4": {
            "info": "search products",
            "func": search_products_menu
        },
        "5": {
            "info": "update a product by id",
            "func": update_product
        },
        "6": {
            "info": "add product",
            "func": add_product
        },
        "7": {
            "info": "delete product by id",
            "func": delete_product_by_id
        }
    })



if __name__ == '__main__':
    product_menu()
