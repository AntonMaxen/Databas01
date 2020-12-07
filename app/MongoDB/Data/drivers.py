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
    product_compatibility = session.query(Compatibility).all()
    for car in car_models:
        car_dict = car.__dict__
        car_dict['car_brand'] = str(car_dict['car_brand'])
        car_dict['model_name'] = str(car_dict['model_name'])
        car_dict['production_year'] = str(car_dict['production_year'])
        car_dict['colour'] = str(car_dict['colour'])
        car_dict['compatibility'] = []
        for pc in product_compatibility:
            if car_dict['id'] == pc.ModelId:
                car_dict['compatibility'].append(pc.ProductId)
        del car_dict['_sa_instance_state']
        del car_dict['id']
        mongo_car_model = mm.CarModel(car_dict)
        mongo_car_model.save()


def fix_associates():
    associates = session.query(Associate).all()
    contact_persson = session.query(ContactPerson).all()
    for associate in associates:
        associate_dict = associate.__dict__
        associate_dict['name'] = str(associate_dict['name'])
        associate_dict['phone'] = str(associate_dict['phone'])
        associate_dict['email'] = str(associate_dict['email'])
        associate_dict['phone'] = str(associate_dict['phone'])
        associate_dict['associates_category'] = str(associate_dict["associates_category"])
        associate_dict['address_line_one'] = str(associate_dict["address_line_one"])
        associate_dict['address_line_two'] = str(associate_dict["address_line_two"])
        associate_dict['zip_code'] = str(associate_dict["zip_code"])
        associate_dict['city'] = str(associate_dict["city"])
        associate_dict['country'] = str(associate_dict["country"])
        for cp in contact_persson:
            if associate_dict['contact_person_id'] == cp.id:
                associate_dict['contact_person'] = {
                    'first_name': cp.first_name,
                    'last_name': cp.last_name,
                    'email': cp.email,
                    'phone': cp.phone
                }
        del associate_dict['id']
        del associate_dict['contact_person_id']
        del associate_dict['_sa_instance_state']

        mongo_associate = mm.Associate(associate_dict)
        mongo_associate.save()


def fix_customers():
    customers = session.query(Customer).all()
    for customer in customers:
        customer_dict = customer.__dict__
        print(customer_dict)


def main():
    #fix_associates()
    #fix_customers()

if __name__ == "__main__":
    main()
