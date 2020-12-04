import app.MySQL.data.repository.shops_repo as sr
from app.MySQL.BL.utils import modelobj_to_dict as mdict


def show_all_shops():
    shops = sr.show_all_shops()
    return [mdict(shop) for shop in shops]


def show_shop_by_id(shop_id):
    shop = sr.show_shop_by_id(shop_id)
    return shop


def show_shop_by_columnvalue(column_name, value):
    shops = sr.show_shop_by_columnvalue(column_name, value)
    return [mdict(shop) for shop in shops]


def update_shop_column(shop, column, value):
    sr.update_shop_column(shop, column, value)


def add_shop(insert_dict):
    sr.add_shop(insert_dict)


def drop_shop(shop_id):
    sr.drop_shop(shop_id)


def get_columns():
    return sr.get_columns()


if __name__ == '__main__':
    show_all_shops()
