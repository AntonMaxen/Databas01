import app.MongoDB.Data.repository.associates_repo as ar


def get_all_associates():
    return ar.get_all_associates()


def get_associate_by_id(a_id):
    return ar.get_associate_by_id(a_id)


def main():
    print(get_all_associates())


if __name__ == '__main__':
    main()
