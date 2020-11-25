from app.data.model_imports import *
import app.data.repository.table_functions as tf


def get_all_order_products():
    return tf.get_all_assets(OrderProduct)


def get_order_product_by_id(c_id, column_name="OrderdId"):
    return tf.get_asset_by_id(OrderProduct, c_id, column_name=column_name)


def get_order_products_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(OrderProduct, column_name, value)


def get_columns():
    return tf.get_columns(OrderProduct)


def update_order_product_column(order_product_obj, column_name, value):
    tf.update_asset_by_column(order_product_obj, column_name, value)


def add_order_product(insert_dict):
    return tf.add_row(OrderProduct, insert_dict)


def drop_order_product(t_id, column_name="OrderId"):
    tf.drop_row_by_id(OrderProduct, t_id, column_name=column_name)


def main():
    update_order_product_column(1, 2, 3)


if __name__ == "__main__":
    main()
