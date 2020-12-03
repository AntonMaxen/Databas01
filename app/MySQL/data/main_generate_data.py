import random
from app.MySqlData.db import session
# dataBuilder imports
from MySQL.dataBuilder.person import Person
from MySQL.dataBuilder.company import CompanyPerson
from MySQL.dataBuilder.car import Car as genCar
from MySQL.dataBuilder.shop import Shop as genShop
from MySQL.dataBuilder.product import Product as genProduct
from MySQL.dataBuilder.contact_person import ContactPerson as genCP
from MySQL.dataBuilder.employee import Employee as genEmployee
from MySQL.dataBuilder.order import Order as genOrder
from MySQL.dataBuilder.storage import Storage as genStorage
from MySQL.dataBuilder.car_model import CarModel as genCarModel
from MySQL.dataBuilder.internal_order import InternalOrder as genInternalOrder
from MySQL.dataBuilder.shops_storage import ShopStorage as genShopStorage
from MySQL.dataBuilder.associate import Associate as genAs
# model imports
from app.MySqlData.model_imports import *


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


def connecting_table(model, generated_data, amount):

    x, y, z = 1, 1, 1
    for _ in range(amount):
        gen = generated_data(x, y, z)
        populate_db(model, gen.__dict__)
        x += 1
        y = random.randrange(1, amount)
        z = random.randrange(1, amount)

    commit_db()


def main():

    quantity = 100

    populate_db_random(Customer, [Person, CompanyPerson], quantity)
    populate_db_random(Car, genCar, quantity)
    populate_db_random(Shop, genShop, quantity)
    populate_db_random(Product, genProduct, quantity)
    populate_db_random(ContactPerson, genCP, quantity)
    populate_db_random(Employee, genEmployee, quantity)
    populate_db_random(Order, genOrder, quantity)
    populate_db_random(Storage, genStorage, quantity)
    populate_db_random(CarModel, genCarModel, quantity)
    populate_db_random(InternalOrder, genInternalOrder, quantity)
    connecting_table(ShopStorage, genShopStorage, quantity)
    populate_db_random(Associate, genAs, quantity)



if __name__ == '__main__':
    main()
