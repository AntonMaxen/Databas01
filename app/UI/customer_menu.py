from app.UI.menus import menu
import app.BL.customer_controller as cc


def f_input():
    return input('> ')


def print_amount_matches(my_list):
    print(f'found {len(my_list)} matches')


def divider():
    print('-' * 20)


def print_dict(my_dict):
    for key, value in my_dict.items():
        print(f'{key}: {value}')


def get_all_customers():
    customers = cc.get_all_customers()
    for customer in customers:
        print_dict(customer)
        divider()

    print_amount_matches(customers)


def get_customer_by_id():
    print("Enter a Customer Id")
    c_id = f_input()
    customer = cc.get_customer_by_id(c_id)
    print_dict(customer)
    divider()


def get_customers_by_name():
    print("Enter a Customer Name")
    c_name = f_input()
    customers = cc.get_customers_by_name(c_name)
    for customer in customers:
        print_dict(customer)
        divider()

    print_amount_matches(customers)


def search_customers_menu():
    def customer_by_column(column):
        return lambda: get_customers_by_columnvalue(column)

    options_dict = {}
    for index, column_name in enumerate(cc.get_columns()):
        options_dict[str(index+1)] = {
            "info": column_name,
            "func": customer_by_column(column_name)
        }

    menu(options_dict)


def get_customers_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    customers = cc.get_customers_by_columnvalue(column_name, name)
    for customer in customers:
        print_dict(customer)
        divider()

    print_amount_matches(customers)


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
        }
    })


if __name__ == '__main__':
    search_customers_menu()
