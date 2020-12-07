from app.MySQL.UI.menus import menu
import app.MySQL.BL.car_controller as cc
from app.MySQL.UI.ui_functions import print_list_of_tablerows, print_amount_matches, f_input, print_tablerow, divider


def get_all_cars():
    cars = cc.get_all_cars()
    print_list_of_tablerows(cars)
    print_amount_matches(cars)


def get_car_by_id():
    print("Enter a id")
    c_id = f_input()
    car = cc.get_car_by_id(c_id)
    if car:
        print_tablerow(car)
    else:
        print("not found")


def search_cars_menu():
    def inner(column):
        return lambda: get_cars_by_columnvalue(column)

    menu({str(i+1): {"info": c, "func": inner(c)} for i, c in enumerate(cc.get_columns())})


def get_cars_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    cars = cc.get_cars_by_columnvalue(column_name, name)
    print_list_of_tablerows(cars)
    print_amount_matches(cars)


def update_car():
    print("enter a car id: ")
    c_id = f_input()
    car = cc.get_car_by_id(c_id)

    def inner(column, car):
        return lambda: update_car_column(column, car)

    menu({str(i + 1): {"info": c, "func": inner(c, car)} for i, c in enumerate(cc.get_columns())})


def update_car_column(column, car):
    print("Enter new value: ")
    value = f_input()
    cc.update_car_column(car, column, value)
    print_tablerow(car)


def add_car():
    insert_dict = {}
    for column in cc.get_columns():
        if column != "id":
            insert_dict[column] = input(f'{column}: ')

    car = cc.add_car(insert_dict)
    if car:
        print_tablerow(car)
        divider()
        return car


def drop_car_by_id():
    print("Enter a id to delete car")
    c_id = f_input()
    cc.drop_car(c_id)


def car_menu():
    menu({
        "1": {
            "info": "get all cars",
            "func": get_all_cars
        },
        "2": {
            "info": "get car by id",
            "func": get_car_by_id
        },
        "3": {
            "info": "search cars",
            "func": search_cars_menu
        },
        "4": {
            "info": "update a car by column",
            "func": update_car
        },
        "5": {
            "info": "add a car",
            "func": add_car
        },
        "6": {
            "info": "drop car by id",
            "func": drop_car_by_id
        }
    })
