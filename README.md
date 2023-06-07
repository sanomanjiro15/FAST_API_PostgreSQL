- pip install -r requirements.txt

# alembic
* alembic is application for migrate (т.е. для того чтобы добавлять таблицы, добавлять изменения в таблицах)
    - alembic init alembic - initialize alembic for application
    - `sqlalchemy.url = postgresql+psycopg2://ilyas:admin123@localhost/ilyas_db` code to alembic.ini file for inspect database 
    - `target_metadata = models.Base.metadata`  code to env.py file for inspect tables
    - 1. alembic revision --autogenerate -m "baseline" - create migration for database with name baseline
    - 2. alembic upgrade head - update database structure by migrations in versions folder

# docker compose command
* depends_on (зависит от сервиса, т.е. запустится после того как выполнится другой сервис)
* docker exec -it 14c5d9385025 /bin/bash (войти в терминале внутрь работающего контейнера)


### Best practice important if
    - developers > 1
    - project include more than > 5-10 classes
    - periodical upgrade project
    - will run the project on the server
