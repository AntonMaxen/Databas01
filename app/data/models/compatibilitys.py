from app.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Compatibility(Base):
    __tablename__ = 'compatibilitys'
    ProductId = sa.Column(sa.Integer, sa.ForeignKey('products.id'), primary_key=True),
    ModelId = sa.Column(sa.Integer, sa.ForeignKey('car_models.id'), primary_key=True),
    products = relationship('Product', back_populates='compatibilitys')
    car_models = relationship('CarModel', back_populates='compatibilitys')

    def __repr__(self):
        return f'Compatibility(=ProductId{self.ProductId} modelId={self.ModelId})'
