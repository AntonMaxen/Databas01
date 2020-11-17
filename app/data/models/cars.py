from app.data.db import Base
import sqlalchemy as sa


class Car(Base):
    __tablename__ = 'cars'

    license_number = sa.Column(sa.Integer, primary_key=True)
    brand_name = sa.Column(sa.String(45), nullable=False)
    model_name = sa.Column(sa.String(100), nullable=False)
    prod_year = sa.Column(sa.Integer, nullable=False)
    color = sa.Column(sa.String(45), nullable=False)
    date = sa.Column(sa.DateTime, nullable=False)
    #  TODO: Make many-> many relations with customers and cars

    def __repr__(self):
        return f'Car(=license_number{self.license_number} model_name={self.model_name}, prod_year={self.prod_year})'