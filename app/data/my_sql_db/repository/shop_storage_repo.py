from app.data.my_sql_db import session
from app.data.model_imports import *
import app.data.my_sql_db.repository.table_functions as tf


def get_all_shop_storages():
    return tf.get_all_assets(ShopStorage)


def get_shop_storage_by_id(c_id, column_name="StorageId"):
    return tf.get_asset_by_id(ShopStorage, c_id, column_name=column_name)


def get_shop_storages_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(ShopStorage, column_name, value)


def get_columns():
    return tf.get_columns(ShopStorage)


def update_shop_storage_column(shop_storage_obj, column_name, value):
    tf.update_asset_by_column(shop_storage_obj, column_name, value)


def add_shop_storage(insert_dict):
    return tf.add_row(ShopStorage, insert_dict)


def drop_shop_storage(t_id, column_name="StorageId"):
    tf.drop_row_by_id(ShopStorage, t_id, column_name=column_name)


def main():
    update_shop_storage_column(1, 2, 3)


if __name__ == "__main__":
    main()
