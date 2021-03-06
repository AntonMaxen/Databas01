import random
import app.MySQL.data.dataBuilder.generator.generate as ge
from app.MySQL.data.db import session
from app.MySQL.data.model_imports import *



class Associate:
    def __init__(self):
        self.name = ge.generate_company_name()
        self.country = 'Sweden'
        self.city = ge.get_random_city("worldcities.csv", self.country)
        self.phone = ge.generate_phone_number(self.country, 9, 'countrycodes.txt')
        self.email = ge.generate_email(self.name, self.city)
        self.address_line_one = ge.generate_address()
        self.address_line_two = self.address_line_one
        self.zip_code = ge.generate_zip()
        self.associates_category = random.choice(['Supplier', 'Manufacturer'])
        self.contact_person_id = session.query(ContactPerson).count()

    def __repr__(self):
        return (
            f'name: {self.name}\n'
            f'phone: {self.phone}\n'
            f'email: {self.email}\n'
            f'addressOne: {self.address_line_one}\n'
            f'addressTwo: {self.address_line_two}\n'
            f'city: {self.city}\n'
            f'zip_code: {self.zip_code}\n'
            f'country: {self.country}\n'
            f'associate_category: {self.associates_category}'
        )


def main():
    associates = [Associate() for _ in range(100)]

    for associate in associates:
        print(associate.__dict__)

if __name__ == '__main__':
    main()


