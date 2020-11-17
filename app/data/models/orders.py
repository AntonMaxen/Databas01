from app.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Order(Base):

    __tablename__ = 'orders'

    id = sa.Column(sa.Integer, primary_key=True)
    total_amount = sa.Column(sa.Integer, nullable=False)
    payment_status = sa.Column(sa.String(100), nullable=False)
    shipping_date = sa.Column(sa.DateTime, nullable=False)
    customer_id = sa.Column(sa.Integer, sa.ForeignKey('customers.id'))
    employee_id = sa.Column(sa.Integer, sa.ForeignKey('employees.id'))
    shop_id = sa.Column(sa.Integer, sa.ForeignKey('shops.id'))
    customers = relationship("Customer", back_populates="orders")
    employees = relationship("Employee", back_populates="orders")
    shops = relationship("Shop", back_populates="orders")
    order_has_products = relationship("OrderProduct", back_populates="orders")

    def __repr__(self):
        return f'Order(id={self.id}, total_amount={self.total_amount}, payment_status={self.payment_status},' \
               f' shipping_date={self.shipping_date}, customer_id={self.customer_id}, ' \
               f'employee_id={self.employee_id}, shop_id={self.shop_id}, customer={self.customer},' \
               f'employee={self.employee}, shop={self.shop})'
