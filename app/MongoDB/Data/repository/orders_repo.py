from app.MongoDB.Data.mongo_models import *
import app.MongoDB.Data.repository.table_functions as tf


def get_all_orders():
    return tf.get_all_assets(Order)


def get_order_by_id(o_id):
    return tf.get_asset_by_id(Order, o_id)


def get_orders_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(Order, column_name, value)


def get_columns():
    return tf.get_columns(Order)


def update_order_column(order_obj, column_name, value):
    tf.update_asset_by_column(order_obj, column_name, value)


def add_order(insert_dict):
    return tf.add_row(Order, insert_dict)


def drop_order(o_id):
    return tf.drop_row_by_id(Order, o_id)


def main():
    print(get_columns())


if __name__ == "__main__":
    main()
