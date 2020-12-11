from app.MongoDB.Data.mongo_models import *
from bson.objectid import ObjectId
from app.MongoDB.Data.db import db


def get_all_assets(mongo_object):
    return mongo_object.all()


def get_asset_by_id(mongo_object, object_id):
    if ObjectId.is_valid(object_id):
        return mongo_object.find(_id=ObjectId(object_id)).first_or_none()


def get_assets_by_columnvalue(mongo_object, column_name, value):
    result = mongo_object.find().first_or_none()
    data_type = getattr(result, column_name, None)
    if isinstance(data_type, int):
        return mongo_object.find(**{column_name: int(value)})
    elif isinstance(data_type, list):
        return []
    elif isinstance(data_type, dict):
        return []
    else:
        if ObjectId.is_valid(value):
            value = ObjectId(value)

        return mongo_object.find(**{
            column_name: {
                "$regex": value
            }
        })


def get_columns(mongo_object):
    dummy_request = mongo_object.find().first_or_none()
    if dummy_request is not None:
        return [key for key in dummy_request.__dict__]
    else:
        return []


def update_asset_by_column(mongo_object, column_name, value):
    result = mongo_object.find().first_or_none()
    data_type = getattr(result, column_name, None)
    if column_name in mongo_object.__dict__:
        if isinstance(data_type, list):
            my_list = getattr(mongo_object, column_name, None)

            if my_list is not None:
                my_list.append(value)
        else:
            setattr(mongo_object, column_name, value)

        mongo_object.save()
        return mongo_object


def add_row(mongo_object, insert_dict):
    return mongo_object.insert_one(insert_dict)


def drop_row_by_id(mongo_object, object_id):
    if ObjectId.is_valid(object_id):
        return mongo_object.delete_one(_id=ObjectId(object_id))


def refresh_row(mongo_object):
    pass


if __name__ == "__main__":
    asset = get_all_assets(Customer)[0]
    update_asset_by_column(asset, "orders", 3)
    print(asset)

