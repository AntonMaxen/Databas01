from app.MongoDB.UI.menus import menu
import app.MongoDB.BL.customer_controller as cc
import app.MongoDB.BL.car_controller as car_controller
from app.MongoDB.BL.utils import modelobj_to_dict
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


def choose_cars():
    cars = []
    c_options = car_controller.get_all_cars()
    running = True
    while running:
        option_dict = {}
        for i, c_option in enumerate(c_options):
            option_dict[str(i)] = c_option._id
            formatted_info = " ".join([f'[{k}={v}]' for k, v in c_option.__dict__.items() if k != "_id" and k != "id"])
            print(f'{i}: {formatted_info}')

        print(f"Currently added cars: [{', '.join([str(car['car_id']) for car in cars])}]")
        w_input = input("> ")
        car_id = option_dict.get(w_input, None)
        if car_id is None:
            running = False
        else:
            car_object = {"car_id": car_id}
            car_object['license_number'] = input("license_number: ")
            car_object['color'] = input("color: ")
            cars.append(car_object)
            print(f"car: {car_object} is added to you")

    return cars


def add_customer():
    insert_dict = {}
    for column in cc.get_columns():
        if column != "_id" and column != "id":
            if column == "cars":
                value = choose_cars()
            elif column == "address_info":
                value = {}
                value["address_line_one"] = input('address_line_one: ')
                value["address_line_two"] = input('address_line_two: ')
                value["zip_code"] = input('zip_code: ')
                value["country"] = input('country: ')
            elif column == "orders":
                value = []
            else:
                value = input(f'{column}: ')

            insert_dict[column] = value
    divider()

    customer = cc.add_customer(insert_dict)
    if customer is not None:
        print_tablerow(customer)


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
