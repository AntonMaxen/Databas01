from app.MySQL.dataBuilder.person import Person
import app.MySQL.dataBuilder.generator.generate as ge


class CompanyPerson(Person):
    def __init__(self):
        super().__init__()
        self.company_name = ge.generate_company_name()
        self.organisation_number = ge.generate_organisation_number()

    def __repr__(self):
        return (
            super().__repr__() +
            f'companyName: {self.company_name}\n'
            f'OrganisationNumber: {self.organisation_number}\n'
        )


def main():
    company_persons = []
    for _ in range(100):
        company_persons.append(CompanyPerson())

    for c in company_persons:
        print(c)


if __name__ == '__main__':
    main()
