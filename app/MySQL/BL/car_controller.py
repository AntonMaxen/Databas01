import app.MySQL.data.repository.cars_repo as cr


def get_all_cars():
    return cr.get_all_cars()


def get_car_by_id(c_id):
    return cr.get_car_by_id(c_id)


def get_cars_by_columnvalue(column_name, value):
    return cr.get_cars_by_columnvalue(column_name, value)


def update_car_column(car, column, value):
    cr.update_car_column(car, column, value)


def add_car(insert_dict):
    return cr.add_car(insert_dict)


def drop_car(t_id):
    cr.drop_car(t_id)


def get_columns():
    return cr.get_columns()
