from app.db import Base, engine, session
from app.dataBuilder.person import Person
from app.dataBuilder.company import CompanyPerson
import random
from app.models.shops import Shop
from app.models.customers import Customer


def add_generated_customer(amount):
    for _ in range(amount):
        variations = [Person, CompanyPerson]
        generated_customer = random.choice(variations)()
        customer = Customer(
            first_name=generated_customer.first_name,
            last_name=generated_customer.last_name,
            phone=generated_customer.phone_number,
            email=generated_customer.email,
            company_name=getattr(generated_customer, "company_name", None),
            organization_number=getattr(generated_customer, "organisation_number", None),
            address_line_one=generated_customer.address_one,
            address_line_two=generated_customer.address_two,
            zip_code=generated_customer.zip,
            city=generated_customer.city,
            country=generated_customer.country
        )
        session.add(customer)

    session.commit()


def main():
    Base.metadata.create_all(engine)
    add_generated_customer(10)


if __name__ == '__main__':
    main()
