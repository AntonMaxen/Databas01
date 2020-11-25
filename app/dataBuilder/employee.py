import random
import app.dataBuilder.generator.generate as gen


class Employee:
    def __init__(self):
        self.first_name = gen.get_random_from_file("names.txt").title()
        self.last_name = gen.get_random_from_file("surnames.txt").title()
        self.job_title = gen.get_random_from_file("job-titles.txt").title()
        self.email = gen.generate_email(self.first_name, self.last_name)
        self.reports_to = 1

    def __repr__(self):
        return (
            f'first_name: {self.first_name}\n'
            f'last_name: {self.last_name}\n'
            f'country: {self.country}\n'
            f'city: {self.city}\n'
            f'zip: {self.zip_code}\n'
            f'addressOne: {self.address_line_one}\n'
            f'addressTwo: {self.address_line_two}\n'
            f'phonenumber: {self.phone}\n'
            f'email: {self.email}\n'
        )


def main():
    employees = []
    for _ in range(100):
        employees.append(Employee())

    for e in employees:
        print(e.__dict__)


if __name__ == '__main__':
    main()
