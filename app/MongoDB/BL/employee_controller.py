import app.MongoDB.Data.repository.employees_repo as er


def get_all_employees():
    return er.get_all_employees()


def get_employee_by_id(e_id):
    return er.get_employee_by_id(e_id)


def get_employee_by_name(e_name):
    return er.get_employee_by_columnvalue("first_name", e_name)


def get_employee_by_columnvalue(column_name, value):
    return er.get_employee_by_columnvalue(column_name, value)


def update_employee_column(employee, column, value):
    er.update_employee_column(employee, column, value)


def add_employee(insert_dict):
    return er.add_employee(insert_dict)


def drop_employee(t_id):
    return er.drop_employee(t_id)


def get_columns():
    return er.get_columns()


if __name__ == '__main__':
    pass

