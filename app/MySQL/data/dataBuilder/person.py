import random
import MySQL.data.dataBuilder.generator.generate as gen


class Person:
    def __init__(self):
        self.first_name = gen.get_random_from_file("names.txt").title()
        self.last_name = gen.get_random_from_file("surnames.txt").title()
        #self.country = get_random_country("countrycodes.txt")
        self.country = "Sweden"
        self.city = gen.get_random_city("worldcities.csv", self.country)
        self.zip_code = gen.generate_zip()
        self.address_line_one = gen.generate_address()
        self.address_line_two = gen.generate_address() if random.randint(0, 1) else None
        self.phone = gen.generate_phone_number(self.country, 9, "countrycodes.txt")
        self.email = gen.generate_email(self.first_name, self.last_name)

    def __repr__(self):
        return (
            f'first_name: {self.first_name}\n'
            f'last_name: {self.last_name}\n'
            f'country: {self.country}\n'
            f'city: {self.city}\n'
            f'zip: {self.zip_code}\n'
            f'addressOne: {self.address_line_one}\n'
            f'addressTwo: {self.address_line_two}\n'
            f'phonenumber: {self.phone}\n'
            f'email: {self.email}\n'
        )


def test_file():
    with open('files/countrycodes.txt', encoding="utf8") as f:
        for line in f:
            if "," not in line:
                print(line)
            else:
                print("ok")


def main():
    persons = []
    for _ in range(100):
        persons.append(Person())

    for p in persons:
        print(p.__dict__)


if __name__ == '__main__':
    main()
