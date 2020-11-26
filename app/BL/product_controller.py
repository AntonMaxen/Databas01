import app.data.repository.products_repo as pr
from app.BL.utils import modelobj_to_dict


def get_all_products():
    return pr.get_all_products()


def get_product_by_id(p_id):
    product = pr.get_product_by_id(p_id)
    return product, modelobj_to_dict(product)


def get_products_by_name(p_name):
    products = pr.get_products_by_columnvalue("product_name", p_name)
    return [modelobj_to_dict(product) for product in products]


def get_products_by_columnvalue(column_name, value):
    products = pr.get_products_by_columnvalue(column_name, value)
    return [modelobj_to_dict(product) for product in products]


def get_columns():
    return pr.get_columns()


def update_product_column(product, column, value):
    pr.update_product_column(product, column, value)


def add_product(insert_dict):
    pr.add_product(insert_dict)


def delete_product(t_id):
    pr.delete_product(t_id)


if __name__ == '__main__':
    pass
