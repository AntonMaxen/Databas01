from app.MySQL.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'products'

    id = sa.Column(sa.Integer, primary_key=True)
    product_name = sa.Column(sa.String(100), nullable=False)
    description = sa.Column(sa.String(2000), nullable=False)
    purchase_price = sa.Column(sa.String(45), nullable=False)
    retail_price = sa.Column(sa.String(100), nullable=False)
    products_has_internal_orders = relationship('ProductInternalOrder', back_populates='products')
    shops_has_storages = relationship('ShopStorage', back_populates='products')
    compatibilities = relationship('Compatibility', back_populates='products')
    orders_has_products = relationship('OrderProduct', back_populates='products')
    pa = relationship('ProductAssociate', back_populates='products')

    def __repr__(self):
        return f'Product(id={self.id}, product_name={self.product_name}, description={self.description},' \
               f'purchase_price={self.purchase_price}, retail_price={self.retail_price})'

