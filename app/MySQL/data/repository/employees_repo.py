from app.MySQL.data.model_imports import *
import app.MySQL.data.repository.table_functions as tf


def get_all_employees():
    return tf.get_all_assets(Employee)


def get_employee_by_id(c_id, column_name="id"):
    return tf.get_asset_by_id(Employee, c_id, column_name=column_name)


def get_employees_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(Employee, column_name, value)


def get_columns():
    return tf.get_columns(Employee)


def update_employee_column(employee_obj, column_name, value):
    tf.update_asset_by_column(employee_obj, column_name, value)


def add_employee(insert_dict):
    return tf.add_row(Employee, insert_dict)


def drop_employee(t_id, column_name="id"):
    tf.drop_row_by_id(Employee, t_id, column_name=column_name)


def main():
    update_employee_column(1, 2, 3)


if __name__ == "__main__":
    main()
