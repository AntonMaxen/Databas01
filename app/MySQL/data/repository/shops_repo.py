from app.MySQL.data.models.shops import Shop
from app.MySQL.data.models.employees import Employee
import app.MySQL.data.repository.table_functions as tf
from app.MySQL.data.db import session
import re


def show_all_shops():
    return tf.get_all_assets(Shop)


def show_shop_by_id(shop_id, column_name="id"):
    return tf.get_asset_by_id(Shop, shop_id, column_name=column_name)


def show_shop_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(Shop, column_name, value)


def update_shop_column(model_obj, column_name, value):
    tf.update_asset_by_column(model_obj, column_name, value)


def add_shop(insert_dict):
    tf.add_row(Shop, insert_dict)


def drop_shop(t_id, column_name="id"):
    tf.drop_row_by_id(Shop, t_id, column_name=column_name)


def get_columns():
    return tf.get_columns(Shop)


def employees_in_shop(s_id):

    employees = session.query(Employee.first_name, Employee.last_name). \
        join(Shop, Shop.id == Employee.shop_id). \
        filter(Employee.shop_id == s_id). \
        all()

    return((str(employees).strip("[]''").replace(',', ''). replace("'", "")))

if __name__ == '__main__':
    get_columns()
