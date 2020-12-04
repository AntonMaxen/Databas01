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

    car_models = session.query(CarModel).all()
    product_compatability = session.query(Compatibility).all()
    for car in car_models:
        car_dict = car.__dict__
        car_dict['car_brand'] = str(car_dict['car_brand'])
        car_dict['model_name'] = str(car_dict['model_name'])
        car_dict['production_year'] = str(car_dict['production_year'])
        car_dict['colour'] = str(car_dict['colour'])
        car_dict['compatability'] = []
        for pc in product_compatability:
            if car_dict['id'] == pc.ModelId:
                car_dict['compatability'].append(pc.ProductId)
        del car_dict['_sa_instance_state']
        del car_dict['id']
        mongo_car_model = mm.CarModel(car_dict)
        mongo_car_model.save()



def main():
    fix_employees()
    fix_car_models()

if __name__ == "__main__":
    main()
