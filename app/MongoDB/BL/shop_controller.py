import app.MongoDB.Data.repository.shops_repo as sr


def get_all_shops():
    return sr.get_all_shops()


def get_shop_by_id(s_id):
    return sr.get_shop_by_id(s_id)


def get_shop_by_columnvalue(column_name, value):
    return sr.get_shop_by_columnvalue(column_name, value)


def update_shop_column(shop, column, value):
    sr.update_shop_column(shop, column, value)


def add_shop(insert_dict):
    return sr.add_shop(insert_dict)


def drop_shop(t_id):
    return sr.drop_shop(t_id)


def get_columns():
    return sr.get_columns()


def update_shops_employee_list(shop, column_name, value):
    return sr.update_shops_employee_list(shop, column_name, value)


if __name__ == '__main__':
    pass

