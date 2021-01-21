from fixture.db import DbFixture

db = DbFixture(host='localhost', name='addressbook', user='root', password='')

try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()
