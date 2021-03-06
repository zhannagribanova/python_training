from model.contact import Contact
from random import randrange
import allure


def test_edit_some_contact(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.create(Contact(firstname="Oleg",
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
                                       notes="Oleg is a good man"))
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        index = randrange(len(old_contacts))
    contact = Contact(firstname="Oleg",
                      middlename="Maksim",
                      lastname="Olesnikov",
                      nickname="maksimolesnikov",
                      photo="C:\\Users\\j.gribanova\\Pictures\\photo_2019-01-28_23-36-11.jpg",
                      title="Title1",
                      company="Apple1",
                      address_company="USA California1",
                      telephone_home="13-13-131",
                      telephone_mobile="891111111112",
                      telephone_work="2-12-123",
                      fax="123-123-123-1231",
                      email1="test11@test.ru",
                      email2="test22@test.ru",
                      email3="test33@test.ru",
                      homepage="https://test1.ru",
                      bday="2", bmonth="January",
                      byear="1991", aday="1",
                      amonth="January",
                      ayear="2031",
                      home_address="Russia, Moscow",
                      telephone_secondary="133",
                      notes="Maksim is a good man")
    contact.identifier = old_contacts[index].identifier
    with allure.step('When I edit the contact %s from the list' % contact):
        app.contact.edit_contact_by_id(contact.identifier, contact)
    with allure.step('Then the new list of contacts is equal to the old list with the replacement of the edited contact'):
        assert len(old_contacts) == app.contact.count()
        new_contacts = db.get_contact_list()
        # replace
        old_contacts[index] = Contact(firstname=contact.firstname, lastname=contact.lastname, identifier=contact.identifier)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
