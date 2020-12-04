import app.MySQL.dataBuilder.generator.generate as gen


class Compatability:
    def __init__(self, x=1, y=1, z=1):
            self.ProductId = x
            self.ModelId = y

    def __repr__(self):
        return (
            gen.build_repr(
                ProductId=self.ProductId,
                ModelId=self.ModelId,
            )
        )


def main():
    items = []
    quantity = 100
    x, y = 1, 1
    for _ in range(quantity):
        items.append(Compatability(x, y))
        x += 1
        y += 1

    for item in items:
        print(item.__dict__)


if __name__ == '__main__':
    main()