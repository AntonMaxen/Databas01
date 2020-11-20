import data.repository.shops_repo as sr


def show_all_shops():
    return sr.show_all_shops


def show_shop_address(shopid):
    return sr.show_shop_address(shopid)


def show_shop_phone(shopid):
    return sr.show_shop_phone(shopid)

