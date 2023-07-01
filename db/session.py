from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, SQLALCHEMY_DATABASE_URI


# url = URL.create(
#     drivername="postgresql+psycopg2",
#     username=POSTGRES_USER,
#     password=POSTGRES_PASSWORD,
#     host=POSTGRES_HOST,
#     port=POSTGRES_PORT,
#     database=POSTGRES_DB
# )
# engine = create_engine(url)  # движок для подключения к БД

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind=engine)


def db_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()