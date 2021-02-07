from model.contact import Contact
import random
import allure


def test_delete_some_contact(app, db, check_ui):
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
        contact = random.choice(old_contacts)
    with allure.step('When I delete the contact %s from the list' % contact):
        app.contact.delete_contact_by_id(contact.identifier)
    with allure.step('Then the new contact list is equal to the old list without the deleted contact'):
        assert len(old_contacts) - 1 == app.contact.count()
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
