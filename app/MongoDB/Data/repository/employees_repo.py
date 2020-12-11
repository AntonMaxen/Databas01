from app.MongoDB.Data.mongo_models import *
import app.MongoDB.Data.repository.table_functions as tf


def get_all_employees():
    return tf.get_all_assets(Employee)


def get_employee_by_id(e_id):
    return tf.get_asset_by_id(Employee, e_id)


def get_employee_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(Employee, column_name, value)


def get_columns():
    return tf.get_columns(Employee)


def update_employee_column(employee_obj, column_name, value):
    tf.update_asset_by_column(employee_obj, column_name, value)


def add_employee(insert_dict):
    return tf.add_row(Employee, insert_dict)


def drop_employee(e_id):
    return tf.drop_row_by_id(Employee, e_id)


def main():
    print(get_columns())


if __name__ == "__main__":
    main()
