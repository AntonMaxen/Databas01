from ..db import Base
import sqlalchemy as sa


class Customer(Base):

    __tablename__ = 'customers'

    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(100), nullable=False)
    last_name = sa.Column(sa.String(100), nullable=False)
    phone = sa.Column(sa.String(45), nullable=False)
    email = sa.Column(sa.String(100), nullable=False)
    company_name = sa.Column(sa.String(100), nullable=True)
    organization_number = sa.Column(sa.String(100), nullable=True)
    address_line_one = sa.Column(sa.String(100), nullable=False)
    address_line_two = sa.Column(sa.String(100), nullable=True)
    zip_code = sa.Column(sa.String(45), nullable=False)
    city = sa.Column(sa.String(100), nullable=False)
    country = sa.Column(sa.String(100), nullable=True)

    def __repr__(self):
        return f'Customer(id={self.id}, first_name={self.first_name}, last_name{self.last_name}, phone={self.phone}, ' \
               f'email={self.email}, company_name={self.company_name}, ' \
               f'organization_number={self.organization_number},' \
               f'address_line_one={self.address_line_one}, address_line_two={self.address_line_two}, ' \
               f'zip_code={self.zip_code}, city={self.city}, country={self.country})'
