from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Storage(Base):
    __tablename__ = 'storages'

    id = sa.Column(sa.Integer, primary_key=True)
    product_amount = sa.Column(sa.String(45), nullable=False)
    min_amount = sa.Column(sa.String(100), nullable=False)
    reorder_amount = sa.Column(sa.Integer, nullable=False)
    shop_id = sa.Column(sa.Integer, sa.ForeignKey('shops.id'))
    shop = relationship('Shop', back_populates='storage')
    # TODO: Make one->one relations work with shop

    def __repr__(self):
        return f'Car(=license_number{self.license_number} model_name={self.model_name}, prod_year={self.prod_year})'