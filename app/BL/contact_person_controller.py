import app.data.repository.contact_persons_repo as cpr


def show_all_cp():
    return cpr.show_all_cp()


def show_cp_by_id(cp_id):
    return cpr.show_cp_by_id(cp_id)


def get_cp_by_columnvalue(column_name, value):
    return cpr.get_cp_by_columnvalue(column_name, value)


def get_columns():
    return cpr.get_columns()


def update_cp_column(contact_person, column, value):
    cpr.update_cp_column(contact_person, column, value)


def add_cp(insert_dict):
    return cpr.add_cp(insert_dict)


def drop_cp(cp_id):
    cpr.drop_cp(cp_id)


if __name__ == '__main__':
    pass
