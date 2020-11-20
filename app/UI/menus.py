def menu(menu_dict):
    running = True
    while running:
        present_menus(menu_dict)
        answer = input('>')
        if answer in menu_dict:
            func = menu_dict[answer].get("func", lambda: None)
            func()
        else:
            print("exiting menu")
            running = False


def present_menus(menu_dict):
    for key, d in menu_dict.items():
        print(f'{key}) {d.get("info", "no description")}')
