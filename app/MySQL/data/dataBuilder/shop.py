import MySQL.data.dataBuilder.generator.generate as ge


class Shop:
    def __init__(self):
        self.country = 'Sweden'
        self.phone = ge.generate_phone_number(self.country, 9, 'countrycodes.txt')
        self.email = ge.generate_email('car', 'spareparts')
        self.address_line_one = ge.generate_address()
        self.address_line_two = self.address_line_one
        self.city = ge.get_random_city("worldcities.csv", self.country)

    def __repr__(self):
        return (
            f'phone: {self.phone}\n'
            f'email: {self.email}\n'
            f'addressOne: {self.address_line_one}\n'
            f'addressTwo: {self.address_line_two}\n'
            f'city: {self.city}\n'
            f'country: {self.country}\n'
        )


def main():
    shops = [Shop() for _ in range(10)]

    for shop in shops:
        print(shop.__dict__)

if __name__ == '__main__':
    main()
