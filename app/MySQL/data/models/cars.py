from app.MySQL.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Car(Base):
    __tablename__ = 'cars'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    brand_name = sa.Column(sa.String(45), nullable=False)
    model_name = sa.Column(sa.String(100), nullable=False)
    prod_year = sa.Column(sa.Integer, nullable=False)
    customers_has_cars = relationship('CustomerCar', back_populates='cars')
    compatibilities = relationship('Compatibility', back_populates='cars')

    def __repr__(self):
        return f'Car(model_name={self.model_name}, prod_year={self.prod_year})'