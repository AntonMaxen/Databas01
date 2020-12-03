import random
import datetime
import MySQL.dataBuilder.generator.generate as gen


class Order:
    def __init__(self):
        self.total_amount = random.randint(50, 5000)
        self.payment_status = random.choice(["pending", "delivered", "waiting for payment"])
        self.shipping_date = datetime.datetime.now()
        self.customer_id = 1
        self.employee_id = 1
        self.shop_id = 1

    def __repr__(self):
        return gen.build_repr(
            total_amount=self.total_amount,
            payment_status=self.payment_status,
            shipping_date=self.shipping_date,
            customer_id=self.customer_id,
            employee_id=self.employee_id,
            shop_id=self.shop_id
        )


def main():
    orders = []
    for _ in range(100):
        orders.append(Order())

    for o in orders:
        print(o)


if __name__ == '__main__':
    main()
