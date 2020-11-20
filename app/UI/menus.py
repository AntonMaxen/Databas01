def menu(menu_dict):
    running = True
    while running:
        present_menus(menu_dict)
        answer = input('>')
        if answer in menu_dict:
            menu = menu_dict[answer]
            menu()
        else:
            print("exiting menu")
            running = False


def present_menus(menu_dict):
    for key, menu in menu_dict.items():
        print(f'{key}) {menu.__name__}')

