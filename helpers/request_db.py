from db import DBClientPerson, Person
from db.session import Session

session = Session()
client = DBClientPerson(session)


def add_family(man_id, woman: Person, kids):
    """
    :param man_id: id of man which added to DB
    :param woman: object of Person
    :param kids: list of Persons
    :return: dictionary, key os firstname lastname, value is id
    """
    res = {}
    kids_ids = []
    for k in kids:
        if k.lastname is None:
            p = client.add_person(k.firstname, "", False)
        else:
            p = client.add_person(k.firstname, k.lastname, False)
        kids_ids.append(p.id)
        res[k.firstname] = p.id
    if woman.lastname is None:
        w = client.add_person(woman.firstname, "", True, spouse_id=man_id, kids_ids=kids_ids)
    else:
        w = client.add_person(woman.firstname, woman.lastname, True, spouse_id=man_id, kids_ids=kids_ids)
    res[woman.firstname] = w.id

    return res