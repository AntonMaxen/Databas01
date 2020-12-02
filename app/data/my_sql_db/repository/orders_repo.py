from app.data.my_sql_db import session
from app.data.model_imports import *
import app.data.my_sql_db.repository.table_functions as tf


def get_all_orders():
    return tf.get_all_assets(Order)


def get_order_by_id(c_id, column_name="id"):
    return tf.get_asset_by_id(Order, c_id, column_name=column_name)


def get_orders_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(Order, column_name, value)


def get_columns():
    return tf.get_columns(Order)


def update_order_column(order_obj, column_name, value):
    tf.update_asset_by_column(order_obj, column_name, value)


def add_order(insert_dict):
    return tf.add_row(Order, insert_dict)


def drop_order(t_id, column_name="id"):
    tf.drop_row_by_id(Order, t_id, column_name=column_name)


def main():
    update_order_column(1, 2, 3)


if __name__ == "__main__":
    main()
