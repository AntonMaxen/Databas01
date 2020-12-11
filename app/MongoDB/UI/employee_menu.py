from app.MongoDB.UI.menus import menu
import app.MongoDB.BL.employee_controller as ec
import app.MongoDB.BL.shop_controller as sc
from app.MongoDB.UI.shop_menu import get_all_shops
from app.MongoDB.UI.ui_functions import f_input, print_amount_matches, divider, print_list_of_tablerows, print_tablerow


def get_all_employees():
    employees = ec.get_all_employees()
    print_list_of_tablerows(employees)
    print_amount_matches(employees)


def get_employee_by_id():
    print("Enter an employee id")
    e_id = f_input()
    employee = ec.get_employee_by_id(e_id)
    print_tablerow(employee)


def get_employee_by_name():
    print("Enter an employee name")
    e_name = f_input()
    employee = ec.get_employee_by_name(e_name)
    print_list_of_tablerows(employee)
    print_amount_matches(employee)


def search_employee_menu():
    def inner(column):
        return lambda: get_employee_by_columnvalue(column)

    menu({str(i+1): {"info": e, "func": inner(e)} for i, e in enumerate(ec.get_columns())})


def get_employee_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    employees = ec.get_employee_by_columnvalue(column_name, name)
    print_list_of_tablerows(employees)
    print_amount_matches(employees)


def update_employee():
    get_all_employees()
    print('====================')
    print("enter an employee id: ")
    e_id = f_input()
    employee = ec.get_employee_by_id(e_id)

    def inner(column, employee):
        return lambda: update_employee_column(column, employee)

    menu({str(i + 1): {"info": e, "func": inner(e, employee)} for i, e in enumerate(ec.get_columns())})


def update_employee_column(column, employee):
    print("Enter new value: ")
    value = f_input()
    ec.update_employee_column(employee, column, value)
    print_tablerow(employee)


def add_employee():
    get_all_shops()
    print('============================================')
    print('Enter a shop id to add employee to that shop')
    s_id = f_input()
    insert_dict = {}
    for column in ec.get_columns():
        if column == 'shop_id':
            insert_dict['shop_id'] = s_id
        elif column != '_id':
            insert_dict[column] = input(f'{column}: ')
    divider()

    employee = ec.add_employee(insert_dict)
    value = employee._id
    if employee is not None:
        shop = sc.get_shop_by_id(s_id)
        sc.update_shop_column(shop, 'employees', value)


def drop_employee_by_id():
    print("Enter an employee id to delete employee")
    e_id = f_input()
    ec.drop_employee(e_id)


def employee_menu():
    menu({
        "1": {
            "info": "get all employees",
            "func": get_all_employees
        },
        "2": {
            "info": "get employees by id",
            "func": get_employee_by_id
        },
        "3": {
            "info": "get employees by name",
            "func": get_employee_by_name
        },
        "4": {
            "info": "search employee",
            "func": search_employee_menu
        },
        "5": {
            "info": "update a employee by id and column",
            "func": update_employee
        },
        "6": {
            "info": "add a employee",
            "func": add_employee
        },
        "7": {
            "info": "drop employee by id",
            "func": drop_employee_by_id
        }
    })


if __name__ == '__main__':
    employee_menu()
