from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Storage(Base):
    __tablename__ = 'storages'

    id = sa.Column(sa.Integer, foreign_key=True)
    product_amount = sa.Column(sa.String(45), nullable=False)
    min_amount = sa.Column(sa.String(100), nullable=False)
    reorder_amount = sa.Column(sa.Integer, nullable=False)
    shop_id = sa.Column(sa.Integer, sa.ForeignKey('shops.id'))
    shop = relationship('Shop', back_populates='storage')


    def __repr__(self):
        return f'Storage(id={self.id}, product_amount={self.product_amount}, min_amount={self.min_amount},' \
               f'reorder_amount={self.reorder_amount}, shop_id={self.shop_id}, shop={self.shop})'
