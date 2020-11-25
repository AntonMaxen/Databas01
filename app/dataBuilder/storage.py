import random
import datetime
import app.dataBuilder.generator.generate as gen


class Storage:
    def __init__(self):
        self.product_amount = random.randint(0, 5000)
        self.min_amount = random.randint(10, 50)
        self.reorder_amount = random.randint(100, 500)

    def __repr__(self):
        return gen.build_repr(
            product_amount=self.product_amount,
            min_amount=self.min_amount,
            reorder_amount=self.reorder_amount
        )


def main():
    storages = []
    for _ in range(100):
        storages.append(Storage())

    for o in storages:
        print(o)


if __name__ == '__main__':
    main()
