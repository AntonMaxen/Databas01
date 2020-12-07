from app.MySQL.data.db import session
from app.MySQL.data.model_imports import *


def get_all_assets(model_obj):
    return session.query(model_obj).all()


def get_asset_by_id(model_obj, t_id, column_name="id"):
    return session.query(model_obj).filter(getattr(model_obj, column_name) == t_id).first()


def get_assets_by_columnvalue(model_obj, column_name, value):
    return session.query(model_obj).filter(getattr(model_obj, column_name).ilike(f'%{value}%')).all()


def get_columns(model_obj):
    return [column.key for column in model_obj.__table__.columns]


def update_asset_by_column(obj, column_name, value):
    try:
        setattr(obj, column_name, value)
        session.commit()
    except:
        print("rollback")
        session.rollback()


def add_row(model_obj, insert_dict):
    try:
        row = model_obj(**insert_dict)
        session.add(row)
        session.commit()
    except:
        print("rollback")
        session.rollback()
        return None

    return row


def refresh_row(row_obj):
    session.refresh(row_obj)


def drop_row_by_id(model_obj, t_id, column_name="id"):
    try:
        session.query(model_obj).filter(getattr(model_obj, column_name) == t_id).delete()
        session.commit()
    except:
        print("rollback")
        session.rollback()

