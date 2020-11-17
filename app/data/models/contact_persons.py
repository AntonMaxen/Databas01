from app.data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class ContactPerson(Base):

    __tablename__ = 'contact_persons'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(45), nullable=False)
    phone = sa.Column(sa.String(45), nullable=False)
    email = sa.Column(sa.String(45), nullable=False)
    category = sa.Column(sa.String(45), nullable=False)
    company_name = relationship('Associates', back_populates='contact_person')

    def __repr__(self):
        return f'ContactPerson(id={self.id}, name={self.name} phone={self.phone}, ' \
               f'email={self.email}, category={self.category}, company_name={self.company_name})'
