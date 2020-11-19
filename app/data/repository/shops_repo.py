from data.models.shops import Shop
from data.db import session


def show_all_shops():
    return session.query(Shop).all()


def show_shop_address(shopid):
    return session.query(Shop).filter(Shop.id == shopid, Shop.address_line_one, Shop.city, Shop.country)


def show_shop_phone(shopid):
    return session.query(Shop).filer(Shop.id == shopid, Shop.phone)
