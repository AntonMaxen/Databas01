import app.data.repository.table_functions as tf


def modelobj_to_dict(modelobj):
    return {name: modelobj.__dict__[name] for name in tf.get_columns(modelobj)}
