import app.MySQL.data.repository.associates_repo as ar


def show_all_associates():
    return ar.show_all_associates()


def show_associate_by_id(a_id):
    return ar.show_associate_by_id(a_id)


def get_associate_by_columnvalue(column_name, value):
    return ar.get_associate_by_columnvalue(column_name, value)


def update_associate_column(associate, column, value):
    ar.update_associate_column(associate, column, value)


def add_associate(insert_dict):
    return ar.add_associate(insert_dict)


def drop_associate(a_id):
    ar.drop_associate(a_id)


def get_columns():
    return ar.get_columns()


if __name__ == '__main__':
    pass

