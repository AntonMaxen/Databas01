from app.data.db import session
from app.data.model_imports import *
import app.data.repository.table_functions as tf


def get_all_customers():
    return tf.get_all_assets(Customer)


def get_customer_by_id(c_id):
    return tf.get_asset_by_id(Customer, c_id)


def get_customers_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(Customer, column_name, value)


def get_columns():
    return tf.get_columns(Customer)


def main():
    pass


if __name__ == "__main__":
    main()
