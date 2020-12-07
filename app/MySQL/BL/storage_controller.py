import app.MySQL.data.repository.storages_repo as cr


def get_all_storages():
    return cr.get_all_storages()


def get_storage_by_id(c_id):
    return cr.get_storage_by_id(c_id)


def get_storages_by_columnvalue(column_name, value):
    return cr.get_storages_by_columnvalue(column_name, value)


def update_storage_column(employee, column, value):
    cr.update_storage_column(employee, column, value)


def add_storage(insert_dict):
    return cr.add_storage(insert_dict)


def drop_storage(t_id):
    cr.drop_storage(t_id)


def get_columns():
    return cr.get_columns()


if __name__ == '__main__':
    pass
