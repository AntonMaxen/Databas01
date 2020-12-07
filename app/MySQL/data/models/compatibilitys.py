from app.MySQL.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Compatibility(Base):
    __tablename__ = 'compatibilitys'

    ProductId = sa.Column(sa.Integer, sa.ForeignKey('products.id'), primary_key=True)
    ModelId = sa.Column(sa.Integer, sa.ForeignKey('cars.id'), primary_key=True)
    products = relationship('Product', back_populates='compatibilities')
    cars = relationship('Car', back_populates='compatibilities')

    def __repr__(self):
        return f'Compatibility(=ProductId{self.ProductId} modelId={self.ModelId})'
