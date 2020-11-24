import app.BL.utils as utils


def f_input():
    return input('---> ')


def print_amount_matches(my_list):
    print(f'found {len(my_list)} matches')


def divider():
    print('-' * 20)


def print_dict(my_dict):
    for key, value in my_dict.items():
        print(f'{key}: {value}')


def print_list_of_tablerows(table_rows):
    for row in table_rows:
        print_tablerow(row)


def print_tablerow(table_row):
    row_dict = utils.modelobj_to_dict(table_row)
    print_dict(row_dict)
    divider()


if __name__ == '__main__':
    pass
