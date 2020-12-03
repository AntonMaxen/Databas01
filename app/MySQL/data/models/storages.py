from app.MySqlData.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Storage(Base):
    __tablename__ = 'storages'

    id = sa.Column(sa.Integer, primary_key=True)
    product_amount = sa.Column(sa.String(45), nullable=False)
    min_amount = sa.Column(sa.String(100), nullable=False)
    reorder_amount = sa.Column(sa.Integer, nullable=False)
    shops_has_storages = relationship('ShopStorage', back_populates='storages')

    def __repr__(self):
        return f'Storage(id={self.id}, product_amount={self.product_amount}, min_amount={self.min_amount},' \
               f'reorder_amount={self.reorder_amount}, shop_id={self.shop_id}, shop={self.shop},' \
               f'shop_has_storages={self.shops_has_storages})'
