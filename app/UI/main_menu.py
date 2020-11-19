from app.UI.menus import main_menus


def main_menu():
    running = True
    while running:
        present_menus(main_menus)
        answer = input('>')
        if answer in main_menus:
            menu = main_menus[answer]
            menu()
        else:
            running = False


def present_menus(menu_dict):
    for key, menu in menu_dict.items():
        print(f'{key}) {menu.__name__}')


if __name__ == "__main__":
    main_menu()
