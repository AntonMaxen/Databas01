from app.MySQL.data.main_generate_data import populate_database
from app.MongoDB.Data.drivers import migrate_to_mongodb


def setup():
    populate_database()
    migrate_to_mongodb()
    

if __name__ == '__main__':
    setup()
