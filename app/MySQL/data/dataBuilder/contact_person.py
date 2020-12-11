import MySQL.data.dataBuilder.generator.generate as ge


class ContactPerson:
    def __init__(self):
        self.first_name = ge.get_random_from_file("names.txt").title()
        self.last_name = ge.get_random_from_file("surnames.txt").title()
        self.phone = ge.generate_phone_number('Sweden', 9, 'countrycodes.txt')
        self.email = ge.generate_email(self.first_name, self.last_name)

    def __repr__(self):
        return (
            f'first_name: {self.first_name}\n'
            f'last_name: {self.last_name}\n'
            f'phone_number: {self.phone}\n'
            f'email: {self.email}\n'
        )


def main():
    contact_persons = [ContactPerson() for _ in range(100)]

    for contact_person in contact_persons:
        print(contact_person.__dict__)


if __name__ == "__main__":
    main()
