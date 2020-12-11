import random
from app.MySQL.data.db import session
# dataBuilder imports
from app.MySQL.data.dataBuilder.person import Person
from app.MySQL.data.dataBuilder.company import CompanyPerson
from app.MySQL.data.dataBuilder.car import Car as genCar
from app.MySQL.data.dataBuilder.shop import Shop as genShop
from app.MySQL.data.dataBuilder.product import Product as genProduct
from app.MySQL.data.dataBuilder.contact_person import ContactPerson as genCP
from app.MySQL.data.dataBuilder.employee import Employee as genEmployee
from app.MySQL.data.dataBuilder.order import Order as genOrder
from app.MySQL.data.dataBuilder.storage import Storage as genStorage
from app.MySQL.data.dataBuilder.internal_order import InternalOrder as genInternalOrder
from app.MySQL.data.dataBuilder.associate import Associate as genAs
# model imports
from app.MySQL.data.model_imports import *


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
    count = session.query(model).count()
    x = count + 1
    y, z = 1, 1
    for _ in range(amount):
        gen = generated_data(x, y, z)
        populate_db(model, gen.__dict__)

        x += 1
        y = random.randrange(1, amount)
        z = random.randrange(1, amount)

    commit_db()


def link_two_tables(table_obj_one={}, table_obj_two={}, relation_table={}, extra_attributes={}):
    # Models
    relation_model = relation_table.get("model", None)
    model_one = table_obj_one.get("model", None)
    model_two = table_obj_two.get("model", None)
    # table rows
    model_arr_one = session.query(model_one).all()
    model_arr_two = session.query(model_two).all()
    relation_arr = session.query(relation_model).all()
    # models ids
    row_one_id = table_obj_one.get("id", None)
    row_two_id = table_obj_two.get("id", None)
    link_attrname_one = relation_table.get("attribute_one", None)
    link_attrname_two = relation_table.get("attribute_two", None)
    for index, row_one in enumerate(model_arr_one):
        if index < len(model_arr_two):
            row_two = model_arr_two[index]
            row_one_value = getattr(row_one, row_one_id, None)
            row_two_value = getattr(row_two, row_two_id, None)
            new_entry = True
            for link_row in relation_arr:
                link_value_one = getattr(link_row, link_attrname_one, None)
                link_value_two = getattr(link_row, link_attrname_two, None)
                if row_one_value == link_value_one and row_two_value == link_value_two:
                    new_entry = False
                    break

            if new_entry:
                insert_dict = {
                    link_attrname_one: row_one_value,
                    link_attrname_two: row_two_value,
                    **extra_attributes
                }
                insertion = relation_model(**insert_dict)
                session.add(insertion)

    session.commit()


def populate_database(quantity=50, generations=1):
    for _ in range(generations):
        populate_db_random(Customer, [Person, CompanyPerson], quantity)
        populate_db_random(Car, genCar, quantity)
        populate_db_random(Shop, genShop, quantity)
        populate_db_random(Product, genProduct, quantity)
        populate_db_random(ContactPerson, genCP, quantity)
        populate_db_random(Employee, genEmployee, quantity)
        populate_db_random(Order, genOrder, quantity)
        populate_db_random(Storage, genStorage, quantity)
        populate_db_random(InternalOrder, genInternalOrder, quantity)
        populate_db_random(Associate, genAs, quantity)

        """
            ##### relational table linking #####
        """
        # Customers_has_cars
        link_two_tables(
            table_obj_one=dict(model=Customer, id="id"),
            table_obj_two=dict(model=Car, id="id"),
            relation_table=dict(model=CustomerCar, attribute_one="CustomerId", attribute_two="CarId")
        )

        # orders_has_products
        link_two_tables(
            table_obj_one=dict(model=Order, id="id"),
            table_obj_two=dict(model=Product, id="id"),
            relation_table=dict(model=OrderProduct, attribute_one="OrderId", attribute_two="ProductId"),
            extra_attributes=dict(Amount=random.randint(50, 500))
        )

        # shops_has_storages
        link_two_tables(
            table_obj_one=dict(model=Shop, id="id"),
            table_obj_two=dict(model=Storage, id="id"),
            relation_table=dict(model=ShopStorage, attribute_one="ShopId", attribute_two="StorageId"),
            extra_attributes=dict(ProductId=session.query(Product).count())
        )

        # products_has_associates
        link_two_tables(
            table_obj_one=dict(model=Product, id="id"),
            table_obj_two=dict(model=Associate, id="id"),
            relation_table=dict(model=ProductAssociate, attribute_one="ProductId", attribute_two="AssociateId"),
        )

        # Compatibility
        link_two_tables(
            table_obj_one=dict(model=Product, id="id"),
            table_obj_two=dict(model=Car, id="id"),
            relation_table=dict(model=Compatibility, attribute_one="ProductId", attribute_two="ModelId")
        )

        # products_has_internal_orders
        link_two_tables(
            table_obj_one=dict(model=Product, id="id"),
            table_obj_two=dict(model=InternalOrder, id="id"),
            relation_table=dict(model=ProductInternalOrder, attribute_one="ProductId", attribute_two="InternalOrderId")
        )


if __name__ == '__main__':
    populate_database()
