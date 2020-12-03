import app.MongoDB.Data.mongo_models as mm
from app.MySQL.data.db import session
from app.MySQL.data.model_imports import *
import random


def fix_employees():
    employees = session.query(Employee).all()
    for employee in employees:
        as_dict = employee.__dict__
        del as_dict['_sa_instance_state']
        as_dict['shop_id'] = random.randint(1, 101)
        if as_dict['reports_to'] is None or as_dict['reports_to'] == as_dict['id']:
            del as_dict['reports_to']

        mongo_employee = mm.Employee(as_dict)

        mongo_employee.save()

    employees = mm.Employee.all()
    for employee in employees:
        if hasattr(employee, 'reports_to'):
            employee.reports_to = mm.Employee.find(id=employee.reports_to).first_or_none()._id
            employee.save()


def main():
    fix_employees()


if __name__ == "__main__":
    main()
