from app.MySQL.data.model_imports import *
import app.MySQL.data.repository.table_functions as tf


def get_all_cars():
    return tf.get_all_assets(Car)


def get_car_by_id(c_id, column_name="id"):
    return tf.get_asset_by_id(Car, c_id, column_name=column_name)


def get_cars_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(Car, column_name, value)


def get_columns():
    return tf.get_columns(Car)


def update_car_column(car_obj, column_name, value):
    tf.update_asset_by_column(car_obj, column_name, value)


def add_car(insert_dict):
    return tf.add_row(Car, insert_dict)


def drop_car(t_id, column_name="id"):
    tf.drop_row_by_id(Car, t_id, column_name=column_name)