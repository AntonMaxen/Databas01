from ..db import Base
import sqlalchemy as sa


class Order(Base):

    __tablename__ = 'orders'

    id = sa.Column(sa.Integer, primary_key=True)
    total_amount = sa.Column(sa.Integer, nullable=False)
    payment_status = sa.Column(sa.String(100), nullable=False)
    shipping_date = sa.Column(sa.DateTime, nullable=False)
    # customer_id = INT, NOT NULL, FOREIGN_KEY
    # employees_id = INT, NOT NULL, FOREIGN_KEY
    # shops_id = INT, NOT NULL, FOREIGN_KEY

    def __repr__(self):
        return f'Order(id={self.id}, total_amount={self.total_amount}, payment_status={self.payment_status},' \
               f' shipping_date={self.shipping_date})'
