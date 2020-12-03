from app.MySqlData.model_imports import *
import app.MySqlData.repository.table_functions as tf


def get_all_product_internal_orders():
    return tf.get_all_assets(ProductInternalOrder)


def get_product_internal_order_by_id(c_id, column_name="InternalOrderId"):
    return tf.get_asset_by_id(ProductInternalOrder, c_id, column_name=column_name)


def get_product_internal_orders_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(ProductInternalOrder, column_name, value)


def get_columns():
    return tf.get_columns(ProductInternalOrder)


def update_product_internal_order_column(product_internal_order_obj, column_name, value):
    tf.update_asset_by_column(product_internal_order_obj, column_name, value)


def add_product_internal_order(insert_dict):
    return tf.add_row(ProductInternalOrder, insert_dict)


def drop_product_internal_order(t_id, column_name="InternalOrderId"):
    tf.drop_row_by_id(ProductInternalOrder, t_id, column_name=column_name)


def main():
    update_product_internal_order_column(1, 2, 3)


if __name__ == "__main__":
    main()
