import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.data.my_sql_db.db_settings import DB_DATABASE, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD


engine = sqlalchemy.create_engine(
    f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}',
    echo=False
)

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
metadata = Base.metadata
