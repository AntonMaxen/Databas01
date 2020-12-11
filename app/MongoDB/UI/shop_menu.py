from app.MongoDB.UI.menus import menu
import app.MongoDB.BL.shop_controller as sc
import app.MongoDB.BL.employee_controller as ec
from app.MongoDB.UI.ui_functions import f_input, print_amount_matches, divider, print_list_of_tablerows, print_tablerow


def get_all_shops():
    shops = sc.get_all_shops()
    print_list_of_tablerows(shops)
    print_amount_matches(shops)


def get_shop_by_id():
    print("Enter a shop id")
    s_id = f_input()
    shop = sc.get_shop_by_id(s_id)
    print_tablerow(shop)


def search_shop_menu():
    def inner(column):
        return lambda: get_shop_by_columnvalue(column)

    menu({str(i+1): {"info": e, "func": inner(e)} for i, e in enumerate(sc.get_columns())})


def get_shop_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    shops = sc.get_shop_by_columnvalue(column_name, name)
    print_list_of_tablerows(shops)
    print_amount_matches(shops)


def update_shop():
    print("enter a shop id: ")
    s_id = f_input()
    shop = sc.get_shop_by_id(s_id)

    def inner(column, shop):
        return lambda: update_shop_column(column, shop)

    menu({str(i + 1): {"info": s, "func": inner(s, shop)} for i, s in enumerate(sc.get_columns())})


def update_shop_column(column, shop):
    print("Enter new value: ")
    value = f_input()
    sc.update_shop_column(shop, column, value)
    print_tablerow(shop)


def add_shop():
    insert_dict = {}
    for column in sc.get_columns():
        if column != '_id' and column != 'id':
            if column == 'employees':
                value = []
            else:
                value = input(f'{column}: ')
            insert_dict[column] = value
    divider()
    sc.add_shop(insert_dict)


def drop_shop_by_id():
    print("Enter a shop id to delete shop")
    s_id = f_input()
    sc.drop_shop(s_id)


def update_employee_list():
    get_all_shops()
    print('===================================')
    print('Enter a shop id to choose that shop')
    s_id = f_input()
    running = True
    while running:
        employees = ec.get_all_employees()
        print_list_of_tablerows(employees)
        print('====================')
        print('Enter employee id to add that to the shop of your choice')
        value = f_input()
        shop = sc.get_shop_by_id(s_id)
        sc.update_shop_column(shop, 'employees', value)
        print('Do you want to add more employees?\n'
              '1: Yes\n'
              '2: No')
        if int(f_input()) == 1:
            continue
        else:
            running = False

def shop_menu():
    menu({
        "1": {
            "info": "get all shops",
            "func": get_all_shops
        },
        "2": {
            "info": "get shop by id",
            "func": get_shop_by_id
        },
        "3": {
            "info": "search shop",
            "func": search_shop_menu
        },
        "4": {
            "info": "update a shop by id and column",
            "func": update_shop
        },
        "5": {
            "info": "update the list of employees",
            "func": update_employee_list
        },
        "6": {
            "info": "add a shop",
            "func": add_shop
        },
        "7": {
            "info": "drop shop by id",
            "func": drop_shop_by_id
        }
    })


if __name__ == '__main__':
    shop_menu()
