import app.MySQL.dataBuilder.generator.generate as gen


class ShopStorage:
    def __init__(self, pid=1, shid=1, stid=1):

            self.ProductId = pid
            self.ShopId = shid
            self.StorageId = stid

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
