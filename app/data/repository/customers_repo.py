from app.data.db import session
from app.data.model_imports import *


def get_all_customers():
    return session.query(Customer).all()


def get_customer_by_id(c_id):
    return session.query(Customer).filter(Customer.id == c_id).first()


def get_customers_by_name(c_name):
    return session.query(Customer).filter(Customer.first_name.ilike(f'%{c_name}%')).all()


def get_customers_by_columnvalue(column_name, name):
    return session.query(Customer).filter(getattr(Customer, column_name).ilike(f'%{name}%')).all()


def get_columns():
    return [customer.key for customer in Customer.__table__.columns]


def main():
    print(get_customers_by_columnvalue("first_name", "anna"))


if __name__ == "__main__":
    main()
