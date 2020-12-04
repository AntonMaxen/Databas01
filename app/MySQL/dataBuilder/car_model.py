import app.MySQL.dataBuilder.generator.generate as gen


class CarModel:
    def __init__(self):
        car_dict = gen.generate_car()
        self.car_brand = car_dict['brand_name']
        self.model_name = car_dict['model']
        self.colour = car_dict['color']
        self.production_year = car_dict['prod_year']

    def __repr__(self):
        return (
            gen.build_repr(
                car_brand=self.car_brand,
                model_name=self.model_name,
                colour=self.colour,
                production_year=self.production_year
            )
        )


def main():
    cars = []
    for _ in range(100):
        cars.append(CarModel())

    for car in cars:
        print(car.__dict__)


if __name__ == '__main__':
    main()
