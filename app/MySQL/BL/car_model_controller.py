import app.MySQL.data.repository.car_models_repo as cr


def get_all_car_models():
    return cr.get_all_car_models()


def get_car_model_by_id(c_id):
    return cr.get_car_model_by_id(c_id)


def get_car_models_by_columnvalue(column_name, value):
    return cr.get_car_models_by_columnvalue(column_name, value)


def update_car_model_column(car_model, column, value):
    cr.update_car_model_column(car_model, column, value)


def add_car_model(insert_dict):
    return cr.add_car_model(insert_dict)


def drop_car_model(t_id):
    cr.drop_car_model(t_id)


def get_columns():
    return cr.get_columns()
