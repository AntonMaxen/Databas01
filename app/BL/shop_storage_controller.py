import app.data.repository.shop_storage_repo as cr


def get_all_shop_storages():
    return cr.get_all_shop_storages()


def get_shop_storage_by_id(c_id):
    return cr.get_shop_storage_by_id(c_id)


def get_shop_storages_by_columnvalue(column_name, value):
    return cr.get_shop_storages_by_columnvalue(column_name, value)


def update_shop_storage_column(shop_storage, column, value):
    cr.update_shop_storage_column(shop_storage, column, value)


def add_shop_storage(insert_dict):
    return cr.add_shop_storage(insert_dict)


def drop_shop_storage_by_id(t_id):
    cr.drop_shop_storage(t_id)


def get_columns():
    return cr.get_columns()


if __name__ == '__main__':
    pass
