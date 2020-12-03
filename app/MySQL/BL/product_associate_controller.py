import app.MySqlData.repository.product_associate_repo as cr


def get_all_product_associates():
    return cr.get_all_product_associates()


def get_product_associate_by_id(c_id):
    return cr.get_product_associate_by_id(c_id)


def get_product_associates_by_columnvalue(column_name, value):
    return cr.get_product_associates_by_columnvalue(column_name, value)


def update_product_associate_column(product_associate, column, value):
    cr.update_product_associate_column(product_associate, column, value)


def add_product_associate(insert_dict):
    return cr.add_product_associate(insert_dict)


def drop_product_associate_by_id(t_id):
    cr.drop_product_associate(t_id)


def get_columns():
    return cr.get_columns()


if __name__ == '__main__':
    pass
