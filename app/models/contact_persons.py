from ..db import Base
import sqlalchemy as sa


class ContactPerson(Base):

    __tablename__ = 'contact_persons'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(45), nullable=False)
    phone = sa.Column(sa.String(45), nullable=False)
    email = sa.Column(sa.String(45), nullable=False)
    category = sa.Column(sa.String(45), nullable=False)

    def __repr__(self):
        return f'ContactPerson(id={self.id}, name={self.name} phone={self.phone}, ' \
               f'email={self.email}, category={self.category})'
