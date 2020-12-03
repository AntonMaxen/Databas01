from app.data.my_sql_db import session
from app.data.model_imports import *
import app.data.my_sql_db.repository.table_functions as tf


def get_all_internal_orders():
    return tf.get_all_assets(InternalOrder)


def get_internal_order_by_id(c_id, column_name="id"):
    return tf.get_asset_by_id(InternalOrder, c_id, column_name=column_name)


def get_internal_orders_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(InternalOrder, column_name, value)


def get_columns():
    return tf.get_columns(InternalOrder)


def update_internal_order_column(internal_order_obj, column_name, value):
    tf.update_asset_by_column(internal_order_obj, column_name, value)


def add_internal_order(insert_dict):
    return tf.add_row(InternalOrder, insert_dict)


def drop_internal_order(t_id, column_name="id"):
    tf.drop_row_by_id(InternalOrder, t_id, column_name=column_name)


def main():
    update_internal_order_column(1, 2, 3)


if __name__ == "__main__":
    main()
