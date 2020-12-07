import app.MySQL.data.repository.orders_repo as cr


def get_all_orders():
    return cr.get_all_orders()


def get_order_by_id(c_id):
    return cr.get_order_by_id(c_id)


def get_orders_by_name(column_name, value):
    return cr.get_orders_by_columnvalue(column_name, value)


def update_order_column(order, column, value):
    cr.update_order_column(order, column, value)


def add_order(insert_dict):
    return cr.add_order(insert_dict)


def drop_order(t_id):
    cr.drop_order(t_id)


def get_columns():
    return cr.get_columns()


if __name__ == '__main__':
    pass

