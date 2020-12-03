import MySQL.dataBuilder.generator.generate as gen
import datetime


class Car:
    def __init__(self):
        car_dict = gen.generate_car()
        self.license_number = car_dict['license_number']
        self.brand_name = car_dict['brand_name']
        self.model_name = car_dict['model']
        self.color = car_dict['color']
        self.prod_year = car_dict['prod_year']
        self.date = datetime.datetime.now()

    def __repr__(self):
        return (
            f'license_number: {self.license_number}\n'
            f'brand_name: {self.brand_name}\n'
            f'model: {self.model}\n'
            f'color: {self.color}\n'
            f'prod_year: {self.prod_year}\n'
        )


def main():
    cars = []
    for _ in range(100):
        cars.append(Car())

    for car in cars:
        print(car.__dict__)


if __name__ == '__main__':
    main()
