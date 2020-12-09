from app.MongoDB.Data.mongo_models import *
import app.MongoDB.Data.repository.table_functions as tf


def get_all_customers():
    return tf.get_all_assets(Customer)


def get_customer_by_id(c_id):
    return tf.get_asset_by_id(Customer, c_id)


def get_customers_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(Customer, column_name, value)


def get_columns():
    return tf.get_columns(Customer)


def update_customer_column(customer_obj, column_name, value):
    tf.update_asset_by_column(customer_obj, column_name, value)


def add_customer(insert_dict):
    return tf.add_row(Customer, insert_dict)


def drop_customer(c_id):
    return tf.drop_row_by_id(Customer, c_id)


def main():
    print(get_columns())


if __name__ == "__main__":
    main()
