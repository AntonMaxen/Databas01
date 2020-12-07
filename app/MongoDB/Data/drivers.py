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


def fix_car_models():

    car_models = session.query(Car).all()
    product_compatability = session.query(Compatibility).all()
    for car in car_models:
        car_dict = car.__dict__
        car_dict['brand_name'] = str(car_dict['brand_name'])
        car_dict['model_name'] = str(car_dict['model_name'])
        car_dict['prod_year'] = str(car_dict['prod_year'])
        car_dict['compatability'] = []
        for pc in product_compatability:
            if car_dict['id'] == pc.ModelId:
                car_dict['compatability'].append(pc.ProductId)
        del car_dict['_sa_instance_state']
        del car_dict['id']
        mongo_car_model = mm.CarModel(car_dict)
        mongo_car_model.save()


def fix_customers():
    customers = session.query(Customer).all()
    for customer in customers:
        customer_dict = customer.__dict__
        print(customer_dict)




def main():
    fix_customers()

if __name__ == "__main__":
    main()
