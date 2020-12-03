from app.data.my_sql_db import Base, metadata
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Car(Base):
    __tablename__ = 'cars'

    license_number = sa.Column(sa.String(45), primary_key=True, unique=True, autoincrement=False)
    brand_name = sa.Column(sa.String(45), nullable=False)
    model_name = sa.Column(sa.String(100), nullable=False)
    prod_year = sa.Column(sa.Integer, nullable=False)
    color = sa.Column(sa.String(45), nullable=False)
    date = sa.Column(sa.DateTime, nullable=False)
    customers_has_cars = relationship('CustomerCar', back_populates='cars')

    def __repr__(self):
        return f'Car(=license_number{self.license_number} model_name={self.model_name}, prod_year={self.prod_year})'