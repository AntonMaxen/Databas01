import random
from app.data.db import Base, engine, session
# dataBuilder imports
from app.dataBuilder.person import Person
from app.dataBuilder.company import CompanyPerson
from app.dataBuilder.car import Car as genCar
# model imports
from app.data.models.customers import Customer
from app.data.models.shops import Shop
from app.data.models.employees import Employee
from app.data.models.orders import Order
from app.data.models.cars import Car
from app.data.models.customers_has_cars import CustomerCar
from app.data.models.products import Product
from app.data.models.order_has_products import OrderProduct
from app.data.models.storages import Storage
from app.data.models.shopStorages import ShopStorage
from app.data.models.contact_persons import ContactPerson
from app.data.models.associates import Associate
from app.data.models.products_has_associates import ProductAssociate
from app.data.models.car_models import CarModel
from app.data.models.compatibilitys import Compatibility
from app.data.models.internal_orders import InternalOrder
from app.data.models.products_has_internal_orders import ProductInternalOrder


# Not needed if using the more generic function for data
def add_generated_customer(amount):
    for _ in range(amount):
        variations = [Person, CompanyPerson]
        generated_customer = random.choice(variations)()
        customer = Customer(
            first_name=generated_customer.first_name,
            last_name=generated_customer.last_name,
            phone=generated_customer.phone,
            email=generated_customer.email,
            company_name=getattr(generated_customer, "company_name", None),
            organisation_number=getattr(generated_customer, "organisation_number", None),
            address_line_one=generated_customer.address_line_one,
            address_line_two=generated_customer.address_line_two,
            zip_code=generated_customer.zip_code,
            city=generated_customer.city,
            country=generated_customer.country
        )
        session.add(customer)

    session.commit()


def populate_db(model, data_dict):
    print(data_dict)
    model_obj = model(**data_dict)
    session.add(model_obj)


def commit_db():
    session.commit()


def populate_db_random(model, data_classes, amount=1):
    # Converts class ref to list if not list of class refs
    if not isinstance(data_classes, list):
        data_classes = [data_classes]

    for _ in range(amount):
        generated_data = random.choice(data_classes)()
        populate_db(model, generated_data.__dict__)

    commit_db()


def main():
    populate_db_random(Customer, [Person, CompanyPerson], 100)
    populate_db_random(Car, genCar, 100)


if __name__ == '__main__':
    main()