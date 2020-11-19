from random import randint
import app.dataBuilder.generator.generate as gen

class Product:
    def __init__(self):
        #prod_dict = gen.generate_car()
        self.product_name = gen.get_random_from_file('car_parts_swedish.txt')
        self.description = gen.get_random_from_file('car_part_gibberish_swedish.txt')
        self.purchase_price = randint(50, 500)
        self.retail_price = randint(550, 5000)

    def __repr__(self):
        return (
            f'product_name: {self.product_name}\n'
            f'purchase_price: {self.purchase_price}\n'
            f'retail_price: {self.retail_price}\n'
        )


def main():
    products = []
    for _ in range(100):
        products.append(Product())

    for product in products:
        print(product.__dict__)


if __name__ == '__main__':
    main()
