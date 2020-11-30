from app.data.db import session
from app.data.model_imports import *
import app.data.repository.table_functions as tf


def show_all_associates():
    return tf.get_all_assets(Associate)


def show_associate_by_id(a_id, column_name="id"):
    return tf.get_asset_by_id(Associate, a_id, column_name=column_name)


def get_associate_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(Associate, column_name, value)


def get_columns():
    return tf.get_columns(Associate)


def update_associate_column(model_obj, column_name, value):
    tf.update_asset_by_column(model_obj, column_name, value)


def add_associate(insert_dict):
    return tf.add_row(Associate, insert_dict)


def drop_associate(t_id, column_name="id"):
    tf.drop_row_by_id(Associate, t_id, column_name=column_name)


def main():
    pass


if __name__ == "__main__":
    pass
