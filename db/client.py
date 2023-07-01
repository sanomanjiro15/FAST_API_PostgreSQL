from typing import Type
from sqlalchemy.orm import Session

from db import Person


class DBClientPerson:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def __syncronize_spouse(self, person: Person) -> None:
        spouse_person = self.get_person_by_id(person.spouse_id)
        if spouse_person:
            self.update_person(spouse_person.id, is_married=True, spouse_id=person.id, kids_ids=person.kids_ids)

    def get_person_by_id(self, person_id: int) -> Person:
        return self.db_session.query(Person).filter(Person.id == person_id).one_or_none()

    def add_person(self, firstname, lastname, is_married, spouse_id=None, kids_ids=None) -> Person:
        db_person = Person(firstname=firstname,
                           lastname=lastname,
                           is_married=is_married,
                           spouse_id=spouse_id,
                           kids_ids=kids_ids)
        self.db_session.add(db_person)
        self.db_session.commit()
        self.db_session.refresh(db_person)
        if db_person.spouse_id:
            self.__syncronize_spouse(db_person)
        return db_person

    def delete_person(self, person_id: int) -> bool:
        person = self.get_person_by_id(person_id)
        if person is None:
            return False
        else:
            self.db_session.delete(person)
            self.db_session.commit()
            return True

    def update_person(self, person_id: int, firstname=None, lastname=None, is_married=None, spouse_id=None,
                      kids_ids=None) -> Person:
        person = self.get_person_by_id(person_id)
        if person:
            person.firstname = firstname if firstname is not None else person.firstname
            person.lastname = lastname if lastname is not None else person.lastname
            person.spouse_id = spouse_id if spouse_id is not None else person.spouse_id
            person.kids_ids = kids_ids if kids_ids is not None else person.kids_ids
            person.is_married = is_married if is_married is not None else person.is_married
            self.db_session.commit()
            self.db_session.refresh(person)
            return person

    def get_persons(self) -> list[Type[Person]]:
        persons = self.db_session.query(Person).all()
        return persons

    def get_persons_by_kid_id(self, kid_id: int) -> list[Person] | None:
        max_kids_count = max([len(k[0]) for k in self.db_session.query(Person.kids_ids).all() if k[0]])
        result = []
        for i in range(1, max_kids_count+1):
            persons = self.db_session.query(Person).filter(Person.kids_ids[i] == kid_id).all()
            if persons:
                result += persons
        return result if len(result) > 0 else None
