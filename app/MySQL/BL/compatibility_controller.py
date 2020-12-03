import app.MySqlData.repository.compatibilitys_repo as cr


def get_all_compatibilitys():
    return cr.get_all_compatibilitys()


def get_compatibility_by_id(c_id):
    return cr.get_compatibility_by_id(c_id)


def get_compatibilitys_by_columnvalue(column_name, value):
    return cr.get_compatibilitys_by_columnvalue(column_name, value)


def update_compatibility_column(employee, column, value):
    cr.update_compatibility_column(employee, column, value)


def add_compatibility(insert_dict):
    return cr.add_compatibility(insert_dict)


def drop_compatibility(t_id):
    cr.drop_compatibility(t_id)


def get_columns():
    return cr.get_columns()


if __name__ == '__main__':
    pass
