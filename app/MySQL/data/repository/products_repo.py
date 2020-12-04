from app.MySQL.data.db import session
from app.MySQL.data.model_imports import *
import app.MySQL.data.repository.table_functions as tf
from sqlalchemy.exc import DatabaseError, CircularDependencyError, TimeoutError
from sqlalchemy import join
from sqlalchemy.sql import select


def get_all_products():
    return tf.get_all_assets(Product)


def get_product_by_id(p_id, column_name='id'):
    return tf.get_asset_by_id(Product, p_id, column_name=column_name)


def get_products_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(Product, column_name, value)


def get_columns():
    return tf.get_columns(Product)


def update_product_column(product_obj, column_name, value):
    tf.update_asset_by_column(product_obj, column_name, value)


def add_product(insert_dict):
    tf.add_row(Product, insert_dict)


def delete_product(t_id, column_name="id"):
    tf.drop_row_by_id(Product, t_id, column_name=column_name)


def product_in_stores_by_id(p_id):

    query = session.query(Shop.city, Shop.address_line_one, Storage.product_amount). \
        join(ShopStorage, Shop.id == ShopStorage.ShopId). \
        join(Storage, Storage.id == ShopStorage.ShopId). \
        filter(ShopStorage.ProductId == p_id). \
        all()

    return query


def main():
    pass


if __name__ == "__main__":
    main()
