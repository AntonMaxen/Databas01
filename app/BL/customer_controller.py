import app.data.repository.customers_repo as cr


def modelobj_to_dict(modelobj):
    return {name: modelobj.__dict__[name] for name in cr.get_columns()}


def get_all_customers():
    customers = cr.get_all_customers()
    return [modelobj_to_dict(customer) for customer in customers]


def get_customer_by_id(c_id):
    customer = cr.get_customer_by_id(c_id)
    return modelobj_to_dict(customer)


def get_customers_by_name(c_name):
    customers = cr.get_customers_by_name(c_name)
    return [modelobj_to_dict(customer) for customer in customers]


def get_customers_by_columnvalue(column_name, name):
    customers = cr.get_customers_by_columnvalue(column_name, name)
    return [modelobj_to_dict(customer) for customer in customers]


def get_columns():
    return cr.get_columns()


if __name__ == '__main__':
    ccustomers = get_all_customers()
    for ccustomer in ccustomers:
        for key, value in ccustomer.items():
            print(f'{key}: {value}')
        print("-" * 30)
