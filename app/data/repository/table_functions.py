from app.data.db import session
from app.data.model_imports import *


def get_all_assets(model_obj):
    return session.query(model_obj).all()


def get_asset_by_id(model_obj, t_id):
    return session.query(model_obj).filter(model_obj.id == t_id).first()


def get_assets_by_columnvalue(model_obj, column_name, value):
    return session.query(model_obj).filter(getattr(model_obj, column_name).ilike(f'%{value}%')).all()


def get_columns(model_obj):
    return [column.key for column in model_obj.__table__.columns]

