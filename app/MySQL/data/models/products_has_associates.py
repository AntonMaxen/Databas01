from app.MySQL.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class ProductAssociate(Base):
    __tablename__ = 'products_has_associates'
    ProductId = sa.Column(sa.Integer, sa.ForeignKey('products.id'), primary_key=True)
    AssociateId = sa.Column(sa.Integer, sa.ForeignKey('associates.id'), primary_key=True)
    associates = relationship('Associate', back_populates='pa')
    products = relationship('Product', back_populates='pa')

    def __repr__(self):
        return f'ProductAssociate(associates_id={self.AssociateId} products_id={self.ProductId},' \
               f'associates={self.associates}, products={self.products})'
