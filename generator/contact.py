from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="")] + \
           [Contact(firstname="Oleg", middlename="Ivan", lastname="Kolesnikov", nickname="olegkolesnikov",
                    photo="C:\\Users\\j.gribanova\\Pictures\\photo_2019-01-28_23-36-11.jpg", title="Title",
                    company="Apple", address_company="USA California", telephone_home="13-13-13",
                    telephone_mobile="89111111111", telephone_work="2-12-12", fax="123-123-123-123",
                    email1="test1@test.ru", email2="test2@test.ru", email3="test3@test.ru", homepage="https://test.ru",
                    amonth="January", ayear="2030", home_address="Russia, Saint-Petersburg", telephone_secondary="13",
                    notes="Oleg is a good man")] + \
           [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                    lastname=random_string("lastname", 10))
            for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
