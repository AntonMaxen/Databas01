def f_input():
    return input('---> ')


def print_amount_matches(my_list):
    print(f'found {len(my_list)} matches')


def divider():
    print('-' * 20)


def print_dict(my_dict):
    for key, value in my_dict.items():
        print(f'{key}: {value}')