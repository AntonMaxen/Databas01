from app.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class InternalOrder(Base):

    __tablename__ = 'internal_orders'

    id = sa.Column(sa.Integer, primary_key=True)
    lead_time = sa.Column(sa.DateTime, nullable=False)
    products_has_internal_orders = relationship('ProductInternalOrder', back_populates='internal_orders')

    def __repr__(self):
        return f'InternalOrder(id={self.id}, lead_time={self.lead_time}, products={self.products})'
