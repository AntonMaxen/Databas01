from app.UI.menus import menu
import app.BL.car_model_controller as cc
from app.UI.ui_functions import print_list_of_tablerows, print_amount_matches, f_input, print_tablerow
import datetime


def get_all_car_models():
    car_models = cc.get_all_car_models()
    print_list_of_tablerows(car_models)
    print_amount_matches(car_models)


def get_car_model_by_id():
    print("Enter a id")
    c_id = f_input()
    car_model = cc.get_car_model_by_id(c_id)
    if car_model:
        print_tablerow(car_model)
    else:
        print("not found")


def search_car_models_menu():
    def inner(column):
        return lambda: get_car_models_by_columnvalue(column)

    menu({str(i+1): {"info": c, "func": inner(c)} for i, c in enumerate(cc.get_columns())})


def get_car_models_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    car_models = cc.get_car_models_by_columnvalue(column_name, name)
    print_list_of_tablerows(car_models)
    print_amount_matches(car_models)


def update_car_model():
    print("enter a car_model id: ")
    c_id = f_input()
    car_model = cc.get_car_model_by_id(c_id)

    def inner(column, car_model):
        return lambda: update_car_model_column(column, car_model)

    menu({str(i + 1): {"info": c, "func": inner(c, car_model)} for i, c in enumerate(cc.get_columns())})


def update_car_model_column(column, car_model):
    print("Enter new value: ")
    value = f_input()
    cc.update_car_model_column(car_model, column, value)
    print_tablerow(car_model)


def add_car_model():
    insert_dict = {}
    for column in cc.get_columns():
        if column != "id":
            insert_dict[column] = input(f'{column}: ')

    car_model = cc.add_car_model(insert_dict)
    if car_model:
        print_tablerow(car_model)

    return car_model


def drop_car_model_by_id():
    print("Enter a id to delete car_model")
    c_id = f_input()
    cc.drop_car_model(c_id)


def car_model_menu():
    menu({
        "1": {
            "info": "get all car_models",
            "func": get_all_car_models
        },
        "2": {
            "info": "get car_model by id",
            "func": get_car_model_by_id
        },
        "3": {
            "info": "search car_models",
            "func": search_car_models_menu
        },
        "4": {
            "info": "update a car_model by column",
            "func": update_car_model
        },
        "5": {
            "info": "add a car_model",
            "func": add_car_model
        },
        "6": {
            "info": "drop car_model",
            "func": drop_car_model_by_id
        }
    })
