import app.data.repository.table_functions as tf
import sqlalchemy as sa
from app.data.db import session


def modelobj_to_dict(modelobj):
    # m = sa.inspect(modelobj)
    refresh_row(modelobj)
    return {name: modelobj.__dict__[name] for name in tf.get_columns(modelobj)}


def refresh_row(modelobj):
    tf.refresh_row(modelobj)
