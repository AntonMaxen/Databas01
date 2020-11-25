import app.data.repository.employees_repo as cr


def get_all_employees():
    return cr.get_all_employees()


def get_employee_by_id(c_id):
    return cr.get_employee_by_id(c_id)


def get_employees_by_name(c_name):
    return cr.get_employees_by_columnvalue("first_name", c_name)


def get_employees_by_columnvalue(column_name, value):
    return cr.get_employees_by_columnvalue(column_name, value)


def update_employee_column(employee, column, value):
    cr.update_employee_column(employee, column, value)


def add_employee(insert_dict):
    return cr.add_employee(insert_dict)


def drop_employee(t_id):
    cr.drop_employee(t_id)


def get_columns():
    return cr.get_columns()


if __name__ == '__main__':
    pass
