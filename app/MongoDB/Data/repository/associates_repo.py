from app.MongoDB.Data.mongo_models import *
import app.MongoDB.Data.repository.table_functions as tf


def get_all_associates():
    return tf.get_all_assets(Associate)

def get_associate_by_id(a_id):
    return tf.get_asset_by_id(Associate, a_id)
