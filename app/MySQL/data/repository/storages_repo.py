from app.MySQL.data.model_imports import *
import app.MySQL.data.repository.table_functions as tf


def get_all_storages():
    return tf.get_all_assets(Storage)


def get_storage_by_id(c_id, column_name="id"):
    return tf.get_asset_by_id(Storage, c_id, column_name=column_name)


def get_storages_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(Storage, column_name, value)


def get_columns():
    return tf.get_columns(Storage)


def update_storage_column(storage_obj, column_name, value):
    tf.update_asset_by_column(storage_obj, column_name, value)


def add_storage(insert_dict):
    return tf.add_row(Storage, insert_dict)


def drop_storage(t_id, column_name="id"):
    tf.drop_row_by_id(Storage, t_id, column_name=column_name)


def main():
    update_storage_column(1, 2, 3)


if __name__ == "__main__":
    main()
