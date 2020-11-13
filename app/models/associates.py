from ..db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Associate(Base):

    __tablename__ = 'associates'

    id = sa.Column(sa.Integer, primary_key=True)
    associates_name = sa.Column(sa.String(100), nullable=False)
    phone = sa.Column(sa.String(45), nullable=False)
    email = sa.Column(sa.String(100), nullable=False)
    address_line_one = sa.Column(sa.String(100), nullable=False)
    address_line_two = sa.Column(sa.String(100), nullable=True)
    zip_code = sa.Column(sa.String(45), nullable=False)
    city = sa.Column(sa.String(100), nullable=False)
    country = sa.Column(sa.String(100), nullable=False)
    associates_role = sa.Column(sa.String(100), nullable=False)
    contact_person_id = sa.Column(sa.Integer, sa.ForeignKey('contact_persons.id'))
    contact_person = relationship('ContactPerson', back_populates='company_name')
    # TODO: Make one->one relations work, add 'company_name' variable in contact_persons.py
    #  company_name = relationship('Associates', back_populates='contact_person')

    def __repr__(self):
        return f'Associate(id={self.id,}, associate_name={self.associates_name}, phone={self.phone},' \
               f'email={self.email}, anddress_line_one={self.address_line_one},' \
               f'address_line_two={self.address_line_two}, zip_code={self.zip_code}, city={self.city},' \
               f'country={self.country}, associates_role={self.associates_role}, ' \
               f'contact_person_id={self.contact_person_id}, contact_person={self.contact_person}'
