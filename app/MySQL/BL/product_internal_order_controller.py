import app.MySqlData.repository.product_internal_order_repo as cr


def get_all_product_internal_orders():
    return cr.get_all_product_internal_orders()


def get_product_internal_order_by_id(c_id):
    return cr.get_product_internal_order_by_id(c_id)


def get_product_internal_orders_by_columnvalue(column_name, value):
    return cr.get_product_internal_orders_by_columnvalue(column_name, value)


def update_product_internal_order_column(product_internal_order, column, value):
    cr.update_product_internal_order_column(product_internal_order, column, value)


def add_product_internal_order(insert_dict):
    return cr.add_product_internal_order(insert_dict)


def drop_product_internal_order_by_id(t_id):
    cr.drop_product_internal_order(t_id)


def get_columns():
    return cr.get_columns()


if __name__ == '__main__':
    pass
