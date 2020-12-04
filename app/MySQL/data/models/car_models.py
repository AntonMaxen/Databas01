from app.MySQL.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class CarModel(Base):
    __tablename__ = 'car_models'

    id = sa.Column(sa.Integer, primary_key=True)
    car_brand = sa.Column(sa.String(100), nullable=False)
    model_name = sa.Column(sa.String(100), nullable=False)
    production_year = sa.Column(sa.String(100), nullable=False)
    colour = sa.Column(sa.String(45), nullable=True)
    compatibilities = relationship('Compatibility', back_populates='car_models')

    def __repr__(self):
        return f'CarModels(id={self.id}, car_brand={self.car_brand}, model_name{self.model_name},' \
               f'production_year={self.production_year}, colour={self.colour},' \
               f' compatibilitys={self.compatibilities})'
