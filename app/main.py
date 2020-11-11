from db import Base, engine, session
from models.shops import Shop


def main():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
