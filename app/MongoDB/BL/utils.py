import app.MongoDB.Data.repository.table_functions as tf


def modelobj_to_dict(modelobj):
    refresh_row(modelobj)
    return {name: modelobj.__dict__[name] for name in tf.get_columns(modelobj)}


def refresh_row(modelobj):
    tf.refresh_row(modelobj)