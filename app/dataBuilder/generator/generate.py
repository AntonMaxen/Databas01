from app.utils import get_project_root
import random
import string
import os


def absolute_path(file_name):
    abs_path = os.path.join(get_project_root(), "app", "dataBuilder", "files")
    return os.path.join(abs_path, file_name)


def get_random_from_file(file_name):
    with open(absolute_path(file_name), encoding="utf8") as f:
        return random.choice([line.strip('\n') for line in f.readlines()])


def get_random_city(file_name, country):
    with open(absolute_path(file_name), encoding="utf8") as f:
        citys = []
        for line in f:
            if country in line:
                citys.append(line.split(',')[1].strip('\n'))

        return random.choice(citys) if len(citys) > 0 else 'unknown'


def get_random_country(file_name):
    with open(absolute_path(file_name), encoding="utf8") as f:
        countries = [line.strip('\n').split(',')[0] for line in f.readlines()]
    return random.choice(countries)


def get_random_street_suffix(file_name):
    return get_random_from_file(file_name).split(',')[0].lower()


def get_call_code(country_name, file_name):
    with open(absolute_path(file_name), encoding='utf8') as f:
        for line in f:
            if country_name in line:
                return line.strip('\n').split(',')[1]


def generate_zip():
    return random.randint(10000, 100000)


def generate_email(first_name, last_name):
    providers = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com"]
    suffix = random.randint(0, 10000)
    return f'{first_name.lower()}.{last_name.lower()}{suffix}@{random.choice(providers)}'


def generate_phone_number(country_name, digits, file_name):
    call_code = get_call_code(country_name, file_name)
    number = "".join([str(random.randint(0, 9)) for _ in range(digits)])
    return f'(+{call_code}){number}'


def generate_address():
    suffix = get_random_street_suffix("streetsuffixes.txt")
    name = get_random_from_file("food-related.txt")
    number = random.randint(1, 101)
    return f'{name.title()}{suffix} {number}'


def generate_company_name():
    suffixes = ["Limited", "Incorported", "Corporation"]
    first = get_random_from_file("generalpicturablewords.txt")
    second = get_random_from_file("generalqualities.txt")
    return f'{first.title()}{second} {random.choice(suffixes)}'


def generate_organisation_number():
    first = random_number_string(6)
    second = random_number_string(4)
    return f'{first}-{second}'


def random_number_string(amount, minimum=0, maximum=9):
    return "".join([str(random.randint(minimum, maximum)) for _ in range(amount)])


def return_random_color(file_name):
    with open(absolute_path(file_name), encoding="utf8") as f:
        colors = [line for line in f]
        color = random.choice(colors)
    return color.rstrip('\n')


def generate_license_plate():
    chars_list = [random.choice(string.ascii_uppercase) for _ in range(3)]
    nums_list = [random.choice(range(1,9)) for _ in range(3)]
    license_plate = ''.join(map(str, chars_list)) + ' ' + ''.join(map(str, nums_list))
    return license_plate


def generate_car():
    with open(absolute_path('carbrands_models.txt'), encoding="utf8") as f:
        cars = []
        for line in f:
            brand_name = line.split(',')[0]
            model = line.split(',')[1].rstrip('\n')
            car = {
                'license_number': generate_license_plate(),
                'brand_name': brand_name,
                'model': model,
                'color': return_random_color('colors.txt'),
                'prod_year': random.choice(range(1990, 2020))
            }
            cars.append(car)
        return random.choice(cars)

def main():
    pass


if __name__ == '__main__':
    main()
