from app.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class ProductInternalOrder(Base):
    __tablename__ = 'products_has_internal_orders'

    ProductId = sa.Column(sa.Integer, sa.ForeignKey('products.id'), primary_key=True)
    InternalOrderId = sa.Column(sa.Integer, sa.ForeignKey('internal_orders.id'), primary_key=True)
    products = relationship('Product', back_populates='products_has_internal_orders')
    internal_orders = relationship('InternalOrder', back_populates='products_has_internal_orders')

    def __repr__(self):
        return f'ProductInternalOrder(ProductId={self.ProductId} InternalOrderId={self.InternalOrderId})'