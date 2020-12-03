from app.data.my_sql_db import session
from app.data.model_imports import *
import app.data.my_sql_db.repository.table_functions as tf


def get_all_product_associates():
    return tf.get_all_assets(ProductAssociate)


def get_product_associate_by_id(c_id, column_name="AssociateId"):
    return tf.get_asset_by_id(ProductAssociate, c_id, column_name=column_name)


def get_product_associates_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(ProductAssociate, column_name, value)


def get_columns():
    return tf.get_columns(ProductAssociate)


def update_product_associate_column(product_associate_obj, column_name, value):
    tf.update_asset_by_column(product_associate_obj, column_name, value)


def add_product_associate(insert_dict):
    print(insert_dict)
    return tf.add_row(ProductAssociate, insert_dict)


def drop_product_associate(t_id, column_name="AssociateId"):
    tf.drop_row_by_id(ProductAssociate, t_id, column_name=column_name)


def main():
    update_product_associate_column(1, 2, 3)


if __name__ == "__main__":
    main()
