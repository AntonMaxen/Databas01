import app.MongoDB.Data.repository.customers_repo as cr


def get_all_customers():
    return cr.get_all_customers()


def get_customer_by_id(c_id):
    return cr.get_customer_by_id(c_id)


def get_customers_by_name(c_name):
    return cr.get_customers_by_columnvalue("first_name", c_name)


def get_customers_by_columnvalue(column_name, value):
    return cr.get_customers_by_columnvalue(column_name, value)


def update_customer_column(customer, column, value):
    cr.update_customer_column(customer, column, value)


def add_customer(insert_dict):
    return cr.add_customer(insert_dict)


def drop_customer(t_id):
    return cr.drop_customer(t_id)


def get_columns():
    return cr.get_columns()


if __name__ == '__main__':
    pass

