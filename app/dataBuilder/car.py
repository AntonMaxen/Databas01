import app.dataBuilder.generator.generate as gen


class Car:
    def __init__(self):
        self.license_number = gen.generate_car()['license_number'] # potentiellt problem... generera unik sträng?
        self.brand_name = gen.generate_car()['brand_name']
        self.model = gen.generate_car()['model']
        self.color = gen.generate_car()['color']
        self.prod_year = gen.generate_car()['prod_year']


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
    for _ in range(10):
        cars.append(Car())

    for car in cars:
        print(car.__dict__)


if __name__ == '__main__':
    main()
