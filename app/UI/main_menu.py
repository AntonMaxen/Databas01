def main_menu():

    running = True

    while running:
        print('Main Menu :::::::::::')
        print('1) Customers')
        print('q) Quit')

        answer = input('>')
        if answer == 'q':
            running = False


if __name__ == "__main__":
    main_menu()
