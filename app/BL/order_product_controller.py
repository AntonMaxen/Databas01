import app.data.repository.order_product_repo as cr


def get_all_order_products():
    return cr.get_all_order_products()


def get_order_product_by_id(c_id):
    return cr.get_order_product_by_id(c_id)


def get_order_products_by_columnvalue(column_name, value):
    return cr.get_order_products_by_columnvalue(column_name, value)


def update_order_product_column(order_product, column, value):
    cr.update_order_product_column(order_product, column, value)


def add_order_product(insert_dict):
    return cr.add_order_product(insert_dict)


def drop_order_product_by_id(t_id):
    cr.drop_order_product(t_id)


def get_columns():
    return cr.get_columns()


if __name__ == '__main__':
    pass
