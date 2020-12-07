import app.MySQL.dataBuilder.generator.generate as gen
import random

class Employee:
    def __init__(self):
        self.first_name = gen.get_random_from_file("names.txt").title()
        self.last_name = gen.get_random_from_file("surnames.txt").title()
        self.job_title = gen.get_random_from_file("job-titles.txt").title()
        self.email = gen.generate_email(self.first_name, self.last_name)
        self.reports_to = 1
        self.shop_id = random.randint(1, 10)

    def __repr__(self):
        return (
            f'first_name: {self.first_name}\n'
            f'last_name: {self.last_name}\n'
            f'job_title: {self.job_title}\n'
            f'email: {self.email}\n'
            f'reports_to: {self.reports_to}\n'
            f'shop_id {self.shop_id}'
        )


def main():
    employees = [Employee() for _ in range(100)]

    for o in employees:
        print(o.__dict__)


if __name__ == '__main__':
    main()
