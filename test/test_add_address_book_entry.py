# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


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
            for i in range(5)
]


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])
def test_add_address_book_entry(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(Contact(firstname=contact.firstname, lastname=contact.lastname, identifier=contact.identifier))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


"""
    contact = Contact(firstname="Oleg",
                      middlename="Ivan",
                      lastname="Kolesnikov",
                      nickname="olegkolesnikov",
                      photo="C:\\Users\\j.gribanova\\Pictures\\photo_2019-01-28_23-36-11.jpg",
                      title="Title",
                      company="Apple",
                      address_company="USA California",
                      telephone_home="13-13-13",
                      telephone_mobile="89111111111",
                      telephone_work="2-12-12",
                      fax="123-123-123-123",
                      email1="test1@test.ru",
                      email2="test2@test.ru",
                      email3="test3@test.ru",
                      homepage="https://test.ru",
                      bday="1", bmonth="January",
                      byear="1990", aday="1",
                      amonth="January",
                      ayear="2030",
                      home_address="Russia, Saint-Petersburg",
                      telephone_secondary="13",
                      notes="Oleg is a good man")
"""
