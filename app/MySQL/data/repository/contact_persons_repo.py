from app.MySQL.data.model_imports import *
import app.MySQL.data.repository.table_functions as tf


def show_all_cp():
    return tf.get_all_assets(ContactPerson)


def show_cp_by_id(cp_id, column_name="id"):
    return tf.get_asset_by_id(ContactPerson, cp_id, column_name=column_name)


def get_cp_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(ContactPerson, column_name, value)


def get_columns():
    return tf.get_columns(ContactPerson)


def update_cp_column(model_obj, column_name, value):
    tf.update_asset_by_column(model_obj, column_name, value)


def add_cp(insert_dict):
    return tf.add_row(ContactPerson, insert_dict)


def drop_cp(t_id, column_name="id"):
    tf.drop_row_by_id(ContactPerson, t_id, column_name=column_name)


def main():
    pass


if __name__ == "__main__":
    pass
