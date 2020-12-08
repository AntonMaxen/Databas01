import app.MongoDB.Data.mongo_models as mm
from app.MySQL.data.db import session
from app.MySQL.data.model_imports import *
import random


def fix_employees():
    employees = session.query(Employee).all()
    for employee in employees:
        as_dict = employee.__dict__
        del as_dict['_sa_instance_state']
        if as_dict['reports_to'] is None or as_dict['reports_to'] == as_dict['id']:
            del as_dict['reports_to']

        mongo_employee = mm.Employee(as_dict)
        mongo_employee.save()

    employees = mm.Employee.all()
    for employee in employees:
        if hasattr(employee, 'reports_to'):
            employee.reports_to = mm.Employee.find(id=employee.reports_to).first_or_none()._id
            employee.save()


def fix_shop():
    shops = session.query(Shop).all()
    employees = mm.Employee.all()
    for shop in shops:
        as_dict = shop.__dict__
        as_dict['employees'] = []
        as_dict = {key: value for key, value in as_dict.items() if value is not None}
        del as_dict['_sa_instance_state']
        mongo_shop = mm.Shop(as_dict)
        mongo_shop.save()
        for employee in employees:
            if shop.id == employee.shop_id:
                as_dict['employees'].append(employee._id)

        mongo_shop.save()


def clean_mongo_models():
    fix_employees()
    fix_shop()
    fix_orders()
    orders = mm.Order.all()
    shops = mm.Shop.all()
    employees = mm.Employee.all()

    for employee in employees:
        for shop in shops:
            if employee.shop_id == shop.id:
                employee.shop_id = shop._id
                employee.save()
    for order in orders:
        for shop in shops:
            if order.shop_id == shop.id:
                order.shop_id = shop._id
                order.save()
    for shop in shops:
        shop.delete_field('id')
    for employee in employees:
        employee.delete_field('id')
    for order in orders:
        order.delete_field('id')


def fix_car_models():
    car_models = session.query(Car).all()
    product_compatability = session.query(Compatibility).all()

    for car in car_models:
        car_dict = car.__dict__
        car_dict['brand_name'] = str(car_dict['brand_name'])
        car_dict['model_name'] = str(car_dict['model_name'])
        car_dict['prod_year'] = str(car_dict['prod_year'])
        car_dict['compatibility'] = []
        for pc in product_compatability:
            if car_dict['id'] == pc.ModelId:
                car_dict['compatibility'].append(pc.ProductId)
        del car_dict['_sa_instance_state']
        mongo_car_model = mm.Car(car_dict)
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
    fix_car_models()
    customers = session.query(Customer).all()
    customer_cars = session.query(CustomerCar).all()
    for customer in customers:
        mongo_customer = dict(
            id=customer.id,
            first_name=customer.first_name,
            last_name=customer.last_name,
            phone=customer.phone,
            email=customer.email,
            company_name=customer.company_name,
            organisation_number=customer.organisation_number,
            address_info=dict(
                address_line_one=customer.address_line_one,
                address_line_two=customer.address_line_two,
                zip_code=customer.zip_code,
                country=customer.country
            )
        )

        mongo_customer['cars'] = [dict(car_id=car._id, license_number=c.license_number, color=c.color)
                            for car in mm.Car.all() for c in customer_cars
                            if c.CustomerId == customer.id and car.id == c.CarId]

        mongo_customer['orders'] = []

        mm.Customer(mongo_customer).save()


def fix_orders():
    orders = session.query(Order).all()
    customers = session.query(Customer).all()

    for order in orders:
        order_dict = order.__dict__
        order_dict['employee_id'] = mm.Employee.find(id=order.employee_id).first_or_none()._id
        del order_dict['_sa_instance_state']
        customer_id = mm.Customer.find(id=order.customer_id).first_or_none()._id
        for customer in customers:
            if order_dict['customer_id'] == customer.id:
                order_dict['customer_info'] = ({
                    'customer_id': customer_id,
                    'first_name': customer.first_name,
                    'last_name': customer.last_name,
                    'address': customer.address_line_one,
                    'phone': customer.phone
                })

        del order_dict['id']
        del order_dict['customer_id']

        mongo_orders = mm.Order(order_dict)
        mongo_orders.save()


def main():
    fix_associates()
    fix_customers()
    clean_mongo_models()


if __name__ == "__main__":
    main()
