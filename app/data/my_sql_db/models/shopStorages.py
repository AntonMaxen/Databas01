from app.data.my_sql_db import Base, metadata
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class ShopStorage(Base):
    __tablename__ = 'shops_has_storages'

    ShopId = sa.Column(sa.Integer, sa.ForeignKey('shops.id'), primary_key=True)
    StorageId = sa.Column(sa.Integer, sa.ForeignKey('storages.id'), primary_key=True)
    ProductId = sa.Column(sa.Integer, sa.ForeignKey('products.id'))

    shops = relationship('Shop', back_populates='shops_has_storages')
    storages = relationship('Storage', back_populates='shops_has_storages')
    products = relationship('Product', back_populates='shops_has_storages')

    def __repr__(self):
        return f'ShopStorage(=ShopId{self.ShopId} StorageId={self.StorageId}' \
               f'ProductId={self.ProductId})'
