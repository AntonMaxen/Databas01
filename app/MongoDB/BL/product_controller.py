import app.MongoDB.Data.repository.products_repo as pr


def get_all_products():
    return pr.get_all_products()


def get_product_by_id(p_id):
    return pr.get_product_by_id(p_id)


def get_products_by_name(p_name):
    return pr.get_products_by_columnvalue("product_name", p_name)


def get_products_by_columnvalue(column_name, value):
    return pr.get_products_by_columnvalue(column_name, value)


def update_product_column(product, column, value):
    pr.update_product_column(product, column, value)


def delete_product(p_id):
    return pr.delete_product(p_id)


def get_columns():
    return pr.get_columns()


def add_product(insert_dict):
    return pr.add_product(insert_dict)


def main():
    print(get_columns())


if __name__ == '__main__':
    main()


