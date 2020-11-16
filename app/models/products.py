from ..db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Product(Base):

    __tablename__ = 'products'

    id = sa.Column(sa.Integer, primary_key=True)
    product_name = sa.Column(sa.String(100), nullable=False)
    description = sa.Column(sa.String(100), nullable=False)
    purchase_price = sa.Column(sa.String(45), nullable=False)
    retail_price = sa.Column(sa.String(100), nullable=False)
    internal_orders = relationship('InternalOrder', back_populate='products')
    storage = relationship('Storage', back_populate='products')
    #  TODO: Make many-> many relations with product and associates.
    #   Make many-> many relations with products and order
    #   Make many-> many relations with products and car_models
    #   Make many-> many relations with products and internal_orders

    def __repr__(self):
        return f'Product(id={self.id}, product_name={self.product_name}, description={self.description},' \
               f'purchase_price={self.purchase_price}, retail_price={self.retail_price}, shops_id={self.shop_id},' \
               f'storage_id={self.storage_id}, internal_orders_id={self.internal_orders_id},' \
               f'internal_orders={self.internal_orders}, shop={self.shop}, storage={self.storage},)'
