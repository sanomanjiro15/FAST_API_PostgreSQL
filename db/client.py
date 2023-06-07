#from datetime import date
from sqlalchemy.orm import Session

from db import Person, Keys


class DBClientPerson:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_person_by_id(self, person_id: int) -> Person:
        return self.db_session.query(Person).filter(Person.id == person_id).one_or_none()

    def add_person(self, firstname, lastname, is_married, spouse_id=None, kids_ids=None) -> Person:
        db_person = Person(
            firstname=firstname,
            lastname=lastname,
            is_married=is_married,
            spouse_id=spouse_id,
            kids_ids=kids_ids
        )
        self.db_session.add(db_person)
        self.db_session.commit()
        self.db_session.refresh(db_person)
        return db_person


class DBClientKeys:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_keys_by_id(self, keys_id: int) -> Keys:
        return self.db_session.query(Keys).filter(Keys.id == keys_id).one_or_none()

    def add_keys(self, code, price) -> Keys:
        db_keys = Keys(
            code=code,
            price=price
        )
        self.db_session.add(db_keys)
        self.db_session.commit()
        self.db_session.refresh(db_keys)
        return db_keys
