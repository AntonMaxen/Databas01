import app.MongoDB.Data.repository.orders_repo as o_r


def get_all_orders():
    return o_r.get_all_orders()


def get_order_by_id(o_id):
    return o_r.get_order_by_id(o_id)


def get_orders_by_columnvalue(column_name, value):
    return o_r.get_orders_by_columnvalue(column_name, value)


def update_order_column(order, column, value):
    o_r.update_order_column(order, column, value)


def add_order(insert_dict):
    return o_r.add_order(insert_dict)


def drop_order(o_id):
    return o_r.drop_order()


def get_columns():
    return o_r.get_columns()


if __name__ == '__main__':
    pass

