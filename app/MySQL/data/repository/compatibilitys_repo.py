from app.MySQL.data.model_imports import *
import app.MySQL.data.repository.table_functions as tf


def get_all_compatibilitys():
    return tf.get_all_assets(Compatibility)


def get_compatibility_by_id(c_id, column_name="ModelId"):
    return tf.get_asset_by_id(Compatibility, c_id, column_name=column_name)


def get_compatibilitys_by_columnvalue(column_name, value):
    return tf.get_assets_by_columnvalue(Compatibility, column_name, value)


def get_columns():
    return tf.get_columns(Compatibility)


def update_compatibility_column(compatibility_obj, column_name, value):
    tf.update_asset_by_column(compatibility_obj, column_name, value)


def add_compatibility(insert_dict):
    return tf.add_row(Compatibility, insert_dict)


def drop_compatibility(t_id, column_name="ModelId"):
    tf.drop_row_by_id(Compatibility, t_id, column_name=column_name)


def main():
    update_compatibility_column(1, 2, 3)


if __name__ == "__main__":
    main()
