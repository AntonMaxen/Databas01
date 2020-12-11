import app.MySQL.BL.shops_controller as sc
from app.MySQL.UI.menus import menu
import app.MySQL.BL.utils as utils


def f_input():
    return input('---> ')


def print_amount_matches(my_list):
    print(f'found {len(my_list)} matches')


def divider():
    print('-' * 20)


def print_dict(my_dict):
    for key, value in my_dict.items():
        print(f'{key}: {value}')


def show_all_shops():
    shops = sc.show_all_shops()
    for shop in shops:
        s_id = shop['id']
        print_dict(shop)
        employees = sc.employees_in_shop(s_id)
        print(f'Employees: {employees}')
        divider()

    print_amount_matches(shops)


def show_shop_by_id():
    print("Enter a Shop Id")
    shop_id = f_input()
    shop = sc.show_shop_by_id(shop_id)
    print_dict(utils.modelobj_to_dict(shop))
    employees = sc.employees_in_shop(shop_id)
    print(f'Employees: {employees}')
    divider()


def search_shops_menu():
    def inner(column):
        return lambda: show_shop_by_columnvalue(column)

    menu({str(i+1): {"info": c, "func": inner(c)} for i, c in enumerate(sc.get_columns())})


def show_shop_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    shops = sc.show_shop_by_columnvalue(column_name, name)
    for shop in shops:
        print_dict(shop)
        divider()

    print_amount_matches(shops)


def update_shop():
    print("enter a Shop id: ")
    shop_id = f_input()
    shop = sc.show_shop_by_id(shop_id)

    def inner(column, shop):
        return lambda: update_shop_column(column, shop)

    menu({str(i + 1): {"info": s, "func": inner(s, shop)} for i, s in enumerate(sc.get_columns())})


def update_shop_column(column, shop):
    print("Enter new value: ")
    value = f_input()
    sc.update_shop_column(shop, column, value)
    print_dict(utils.modelobj_to_dict(shop))
    divider()


def add_shop():
    insert_dict = {}
    for column in sc.get_columns():
        if column != "id":
            insert_dict[column] = input(f'{column}: ')

    sc.add_shop(insert_dict)


def drop_shop_by_id():
    print("Enter a shop id to delete shop")
    shop_id = int(f_input())
    sc.drop_shop(shop_id)


def shop_menu():

    menu({
        "1": {
            "info": "show all shops",
            "func": show_all_shops
        },
        "2": {
            "info": "show shop by id",
            "func": show_shop_by_id
        },
        "3": {
            "info": "search shops",
            "func": search_shops_menu
        },
        "4": {
            "info": "update a shop by id and column",
            "func": update_shop
        },
        "5": {
            "info": "add a shop",
            "func": add_shop
        },
        "6": {
            "info": "drop shop by id",
            "func": drop_shop_by_id
        }
    })
