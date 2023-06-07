from db import DBClientPerson, DBClientKeys
from db.session import Session

session = Session()
client = DBClientPerson(session)
print(client.get_person_by_id(1))
client.add_person("ilyas", "Niyazov", True, 2, [4, 9])
print(client.get_person_by_id(1))

keys_client = DBClientKeys(session)
keys_client.add_keys(code="123443121", price=150)
