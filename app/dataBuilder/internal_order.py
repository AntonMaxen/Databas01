import random
import datetime
import app.dataBuilder.generator.generate as gen


class InternalOrder:
    def __init__(self):
        self.lead_time = datetime.datetime.now()

    def __repr__(self):
        return gen.build_repr(
            lead_time=self.lead_time
        )


def main():
    internal_orders = []
    for _ in range(100):
        internal_orders.append(InternalOrder())

    for o in internal_orders:
        print(o)


if __name__ == '__main__':
    main()
