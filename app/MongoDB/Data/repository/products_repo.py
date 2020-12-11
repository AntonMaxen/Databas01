from app.MongoDB.Data.mongo_models import *
import app.MongoDB.Data.repository.table_functions as tf


def get_all_products():
    return tf.get_all_assets(Product)


def get_product_by_id(p_id):
    return tf.get_asset_by_id(Product, p_id)


def get_products_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(Product, column_name, value)


def update_product_column(product_obj, column_name, value):
    tf.update_asset_by_column(product_obj, column_name, value)


def delete_product(p_id):
    return tf.drop_row_by_id(Product, p_id)


def get_columns():
    return tf.get_columns(Product)


def main():
    print(get_columns())


if __name__ == "__main__":
    main()
