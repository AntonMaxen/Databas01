from pathlib import Path


def get_project_root():
    return Path(__file__).parent.parent


def main():
    print(get_project_root())
    pass


if __name__ == '__main__':
    main()
