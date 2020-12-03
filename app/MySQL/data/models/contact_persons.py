from app.MySqlData.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class ContactPerson(Base):
    __tablename__ = 'contact_persons'

    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(45), nullable=False)
    last_name = sa.Column(sa.String(45), nullable=False)
    phone = sa.Column(sa.String(45), nullable=False)
    email = sa.Column(sa.String(45), nullable=False)
    company_names = relationship('Associate', back_populates='contact_persons')

    def __repr__(self):
        return f'ContactPerson(id={self.id}, first_name={self.first_name}, last_name={self.last_name},' \
               f' phone={self.phone}, email={self.email}, company_name={self.company_names})'
