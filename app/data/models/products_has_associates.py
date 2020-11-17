from app.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class ProductAssociate(Base):
    __tablename__ = 'products_has_associates'
    associates_id = sa.Column(sa.Integer, sa.ForeignKey('associates.id'), primary_key=True)
    products_id = sa.Column(sa.Integer, sa.ForeignKey('products.id'), primary_key=True)
    associates = relationship('Associate', back_populates='associates_products')
    products = relationship('Product', back_populates='products_has_associates')

    def __repr__(self):
        return f'ProductAssociate(associates_id={self.associates_id} products_id={self.products_id},' \
               f'associates={self.associates}, products={self.products})'
