import app.data.repository.shops_repo as sr
from app.data.model_imports import *


def show_all_shops():
    rows = sr.show_all_shops()
    for index, row in enumerate(rows):
        print(f'{row.id}: phone: {row.phone}, address: {row.address_line_one}')


def show_shop_address(shopid):
    return sr.show_shop_address(shopid)


def show_shop_phone(shopid):
    return sr.show_shop_phone(shopid)


if __name__ == '__main__':
    show_all_shops()