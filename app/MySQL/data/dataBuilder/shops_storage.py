import app.MySQL.data.dataBuilder.generator.generate as gen


class ShopStorage:
    def __init__(self, x=1, y=1, z=1):

            self.ProductId = y
            self.ShopId = x
            self.StorageId = z

    def __repr__(self):
        return (
            gen.build_repr(
                ShopId=self.ShopId,
                StorageId=self.StorageId,
                ProductId=self.ProductId,
            )
        )


def main():
    items = []
    quantity = 100
    x, y, z = 1, 1, 1
    for _ in range(quantity):
        items.append(ShopStorage(x, y, z))
        x += 1
        y += 1
        z += 1


    for item in items:
        print(item.__dict__)


if __name__ == '__main__':
    main()
