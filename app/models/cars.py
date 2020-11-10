from db import Base
import sqlalchemy as sa


class Car(Base):
    __tablename__ = 'cars'

    license_number = sa.Column(sa.Integer, primary_key=True)
    brand_name = sa.Column(sa.String(45))
    model_name = sa.Column(sa.String(100))
    prod_year = sa.Column(sa.Integer)
    color = sa.Column(sa.String(45))
    date = sa.Column(sa.DateTime)

    @property
    def __repr__(self):
        return f'Car(=license_number{self.license_number} model_name={self.model_name}, prod_year={self.prod_year})'