import app.MySqlData.repository.customer_car_repo as cr


def get_all_customer_cars():
    return cr.get_all_customer_cars()


def get_customer_car_by_id(c_id):
    return cr.get_customer_car_by_id(c_id)


def get_customer_cars_by_columnvalue(column_name, value):
    return cr.get_customer_cars_by_columnvalue(column_name, value)


def update_customer_car_column(customer_car, column, value):
    cr.update_customer_car_column(customer_car, column, value)


def add_customer_car(insert_dict):
    return cr.add_customer_car(insert_dict)


def drop_customer_car_by_license_number(t_id):
    cr.drop_customer_car(t_id)


def get_columns():
    return cr.get_columns()


if __name__ == '__main__':
    pass

