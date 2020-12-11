from app.MongoDB.Data.mongo_models import *
import app.MongoDB.Data.repository.table_functions as tf


def get_all_shops():
    return tf.get_all_assets(Shop)


def get_shop_by_id(s_id):
    return tf.get_asset_by_id(Shop, s_id)


def get_shop_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(Employee, column_name, value)


def get_columns():
    return tf.get_columns(Shop)


def update_shop_column(shop_obj, column_name, value):
    tf.update_asset_by_column(shop_obj, column_name, value)


def add_shop(insert_dict):
    return tf.add_row(Shop, insert_dict)


def drop_shop(s_id):
    return tf.drop_row_by_id(Shop, s_id)


def test():
    pass

if __name__ == "__main__":
    test()
