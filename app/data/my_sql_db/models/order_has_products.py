from app.data.my_sql_db import Base, metadata
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class OrderProduct(Base):
    __tablename__ = 'orders_has_products'

    OrderId = sa.Column(sa.Integer, sa.ForeignKey('orders.id'), primary_key=True)
    ProductId = sa.Column(sa.Integer, sa.ForeignKey('products.id'), primary_key=True)
    Amount = sa.Column(sa.Integer, nullable=False)
    products = relationship('Product', back_populates='orders_has_products')
    orders = relationship('Order', back_populates='orders_has_products')

    def __repr__(self):
        return f'OrderProduct(OrderId={self.OrderId} ProductId={self.ProductId}' \
               f'Amount={self.Amount})'
