from app.MySqlData.models.shops import Shop
from app.MySqlData.db import session
import app.MySqlData.repository.table_functions as tf


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


if __name__ == '__main__':
    show_all_shops()
