from app.MySQL.data.model_imports import *
import app.MySQL.data.repository.table_functions as tf


def get_all_customer_cars():
    return tf.get_all_assets(CustomerCar)


def get_customer_car_by_id(c_id, column_name="id"):
    return tf.get_asset_by_id(CustomerCar, c_id, column_name=column_name)


def get_customer_cars_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(CustomerCar, column_name, value)


def get_columns():
    return tf.get_columns(CustomerCar)


def update_customer_car_column(customer_car_obj, column_name, value):
    tf.update_asset_by_column(customer_car_obj, column_name, value)


def add_customer_car(insert_dict):
    return tf.add_row(CustomerCar, insert_dict)


def drop_customer_car(t_id, column_name="license_number"):
    tf.drop_row_by_id(CustomerCar, t_id, column_name=column_name)


def main():
    update_customer_car_column(1, 2, 3)


if __name__ == "__main__":
    main()
