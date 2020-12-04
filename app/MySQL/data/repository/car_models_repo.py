from app.MySQL.data.model_imports import *
import app.MySQL.data.repository.table_functions as tf


def get_all_car_models():
    return tf.get_all_assets(CarModel)


def get_car_model_by_id(c_id, column_name="id"):
    return tf.get_asset_by_id(CarModel, c_id, column_name=column_name)


def get_car_models_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(CarModel, column_name, value)


def get_columns():
    return tf.get_columns(CarModel)


def update_car_model_column(car_model_obj, column_name, value):
    tf.update_asset_by_column(car_model_obj, column_name, value)


def add_car_model(insert_dict):
    return tf.add_row(CarModel, insert_dict)


def drop_car_model(t_id, column_name="id"):
    tf.drop_row_by_id(CarModel, t_id, column_name=column_name)


def main():
    pass


if __name__ == "__main__":
    main()
