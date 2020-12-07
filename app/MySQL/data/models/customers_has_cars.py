from app.MySQL.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class CustomerCar(Base):
    __tablename__ = 'customers_has_cars'

    CustomerId = sa.Column(sa.Integer, sa.ForeignKey('customers.id'), primary_key=True)
    CarId = sa.Column(sa.Integer, sa.ForeignKey('cars.id'), primary_key=True)
    license_number = sa.Column(sa.String(45))
    color = sa.Column(sa.String(45))
    customers = relationship('Customer', back_populates='customers_has_cars')
    cars = relationship('Car', back_populates='customers_has_cars')

    def __repr__(self):
        return f'CustomerCar(CustomerId{self.CustomerId})'