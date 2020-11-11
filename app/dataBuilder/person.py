import random


class Person:
    def __init__(self):
        self.first_name = get_random_from_file("names.txt").title()
        self.last_name = get_random_from_file("surnames.txt").title()
        #self.country = get_random_country("countrycodes.txt")
        self.country = "Sweden"
        self.city = get_random_city("worldcities.csv", self.country)
        self.zip = get_random_zip()
        self.address = create_address()
        self.phone_number = create_phone_number(self.country, 9, "countrycodes.txt")
        self.email = create_email(self.first_name, self.last_name)

    def __repr__(self):
        return (
            f'first_name: {self.first_name}\n'
            f'last_name: {self.last_name}\n'
            f'country: {self.country}\n'
            f'city: {self.city}\n'
            f'zip: {self.zip}\n'
            f'address: {self.address}\n'
            f'phonenumber: {self.phone_number}\n'
            f'email: {self.email}\n'
        )


def get_random_from_file(file_name):
    with open(f'files/{file_name}', encoding="utf8") as f:
        return random.choice([line.strip('\n') for line in f.readlines()])


def get_random_city(file_name, country):
    with open(f'files/{file_name}', encoding="utf8") as f:
        citys = []
        for line in f:
            if country in line:
                citys.append(line.split(',')[1].strip('\n'))

        return random.choice(citys) if len(citys) > 0 else 'unknown'

def get_random_zip():
    return random.randint(10000, 100000)


def get_random_country(file_name):
    with open(f'files/{file_name}', encoding="utf8") as f:
        countries = [line.strip('\n').split(',')[0] for line in f.readlines()]
    return random.choice(countries)


def get_random_street_suffix(file_name):
    return get_random_from_file(file_name).split(',')[0].lower()


def get_call_code(country_name, file_name):
    with open(f'files/{file_name}', encoding='utf8') as f:
        for line in f:
            if country_name in line:
                return line.strip('\n').split(',')[1]


def create_email(first_name, last_name):
    providers = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com"]
    suffix = random.randint(0, 10000)
    return f'{first_name.lower()}.{last_name.lower()}{suffix}@{random.choice(providers)}'


def create_phone_number(country_name, digits, file_name):
    call_code = get_call_code(country_name, file_name)
    print(type(call_code))
    number = "".join([str(random.randint(0, 9)) for _ in range(digits)])
    return f'(+{call_code}){number}'


def create_address():
    suffix = get_random_street_suffix("streetsuffixes.txt")
    name = get_random_from_file("food-related.txt")
    number = random.randint(1, 101)
    return f'{name.title()}{suffix} {number}'


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
        print(p)


if __name__ == '__main__':
    main()
