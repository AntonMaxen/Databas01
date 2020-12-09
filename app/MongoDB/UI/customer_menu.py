from app.MongoDB.UI.menus import menu
import app.MongoDB.BL.customer_controller as cc
#from app.MongoDB.UI.car_menu import add_car
#from app.MongoDB.UI.customer_car_menu import combine_customer_car
from app.MongoDB.UI.ui_functions import f_input, print_amount_matches, divider, print_list_of_tablerows, print_tablerow


def get_all_customers():
    customers = cc.get_all_customers()
    print_list_of_tablerows(customers)
    print_amount_matches(customers)


def get_customer_by_id():
    print("Enter a Customer Id")
    c_id = f_input()
    customer = cc.get_customer_by_id(c_id)
    print_tablerow(customer)


def get_customers_by_name():
    print("Enter a Customer Name")
    c_name = f_input()
    customers = cc.get_customers_by_name(c_name)
    print_list_of_tablerows(customers)
    print_amount_matches(customers)


def search_customers_menu():
    def inner(column):
        return lambda: get_customers_by_columnvalue(column)

    menu({str(i+1): {"info": c, "func": inner(c)} for i, c in enumerate(cc.get_columns())})


def get_customers_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    customers = cc.get_customers_by_columnvalue(column_name, name)
    print_list_of_tablerows(customers)
    print_amount_matches(customers)


def update_customer():
    print("enter a customer id: ")
    c_id = f_input()
    customer = cc.get_customer_by_id(c_id)

    def inner(column, customer):
        return lambda: update_customer_column(column, customer)

    menu({str(i + 1): {"info": c, "func": inner(c, customer)} for i, c in enumerate(cc.get_columns())})


def update_customer_column(column, customer):
    print("Enter new value: ")
    value = f_input()
    cc.update_customer_column(customer, column, value)
    print_tablerow(customer)


def add_customer_car(customer):
    car = add_car()
    if car:
        combine_customer_car(customer.id, car.id)


def bind_add_customer_car(customer):
    return lambda: add_customer_car(customer)


def add_customer():
    insert_dict = {}
    for column in cc.get_columns():
        if column != "id":
            insert_dict[column] = input(f'{column}: ')
    divider()

    customer = cc.add_customer(insert_dict)
    if customer:
        print_tablerow(customer)
        menu({
            "1": {
                "info": "add car",
                "func": bind_add_customer_car(customer)
            }
        })


def drop_customer_by_id():
    print("Enter a customer id to delete customer")
    c_id = f_input()
    cc.drop_customer(c_id)


def customer_menu():
    menu({
        "1": {
            "info": "get all customers",
            "func": get_all_customers
        },
        "2": {
            "info": "get customer by id",
            "func": get_customer_by_id
        },
        "3": {
            "info": "get customers by name",
            "func": get_customers_by_name
        },
        "4": {
            "info": "search customers",
            "func": search_customers_menu
        },
        "5": {
            "info": "update a customer by id and column",
            "func": update_customer
        },
        "6": {
            "info": "add a customer",
            "func": add_customer
        },
        "7": {
            "info": "drop customer by id",
            "func": drop_customer_by_id
        }
    })


if __name__ == '__main__':
    customer_menu()
