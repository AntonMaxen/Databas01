from app.MySQL.UI.menus import menu
import app.MySQL.BL.employee_controller as cc
from app.MySQL.UI.ui_functions import f_input, print_amount_matches, divider, print_list_of_tablerows, print_tablerow


def get_all_employees():
    employees = cc.get_all_employees()
    print_list_of_tablerows(employees)
    print_amount_matches(employees)


def get_employee_by_id():
    print("Enter a Employee Id")
    c_id = f_input()
    employee = cc.get_employee_by_id(c_id)
    print_tablerow(employee)


def get_employees_by_name():
    print("Enter a Employee Name")
    c_name = f_input()
    employees = cc.get_employees_by_name(c_name)
    print_list_of_tablerows(employees)
    print_amount_matches(employees)


def search_employees_menu():
    def inner(column):
        return lambda: get_employees_by_columnvalue(column)

    menu({str(i+1): {"info": c, "func": inner(c)} for i, c in enumerate(cc.get_columns())})


def get_employees_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    employees = cc.get_employees_by_columnvalue(column_name, name)
    print_list_of_tablerows(employees)
    print_amount_matches(employees)


def update_employee():
    print("enter a employee id: ")
    c_id = f_input()
    employee = cc.get_employee_by_id(c_id)

    def inner(column, employee):
        return lambda: update_employee_column(column, employee)

    menu({str(i + 1): {"info": c, "func": inner(c, employee)} for i, c in enumerate(cc.get_columns())})


def update_employee_column(column, employee):
    print("Enter new value: ")
    value = f_input()
    cc.update_employee_column(employee, column, value)
    print_tablerow(employee)


def add_employee():
    insert_dict = {}
    for column in cc.get_columns():
        if column != "id":
            insert_dict[column] = input(f'{column}: ')
    divider()

    employee = cc.add_employee(insert_dict)


def drop_employee_by_id():
    print("Enter a employee id to delete employee")
    c_id = int(f_input())
    cc.drop_employee(c_id)


def employee_menu():
    menu({
        "1": {
            "info": "get all employees",
            "func": get_all_employees
        },
        "2": {
            "info": "get employee by id",
            "func": get_employee_by_id
        },
        "3": {
            "info": "get employees by name",
            "func": get_employees_by_name
        },
        "4": {
            "info": "search employees",
            "func": search_employees_menu
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
