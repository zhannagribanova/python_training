# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest


@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])
def test_add_address_book_entry(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(Contact(firstname=contact.firstname, lastname=contact.lastname, identifier=contact.identifier))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
