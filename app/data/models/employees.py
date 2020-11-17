from app.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Employee(Base):
    __tablename__ = 'employees'
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(100), nullable=False)
    last_name = sa.Column(sa.String(100), nullable=False)
    job_title = sa.Column(sa.String(45), nullable=False)
    email = sa.Column(sa.String(45), nullable=False)
    reports_to = sa.Column(sa.Integer, nullable=False)
    shop_id = sa.Column(sa.Integer, sa.ForeignKey('shops.id'))
    shops = relationship('Shop', back_populates='employees')
    orders = relationship("Order", back_populates="employees")

    def __repr__(self):
        return f'Employee(id={self.id}, first_name={self.first_name}, last_name={self.last_name},' \
               f' job_title={self.job_title}, email={self.email}, reports_to={self.reports_to},' \
               f' shop_id={self.shop_id}, shops={self.shops}, orders={self.orders})'
