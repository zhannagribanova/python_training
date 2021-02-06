from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host='localhost', name='addressbook', user='root', password='')

try:
    l = db.contacts_not_in_group(Group(identifier='120'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass  # db.destroy()
