# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random
import allure


def test_del_contact_from_group(app, orm, check_ui):
    with allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.create(Contact(firstname="Oleg",
                                       middlename="Ivanovich",
                                       lastname="Ivanov",
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
        contacts = orm.get_contact_list()
    with allure.step('Given a non-empty group list'):
        if app.group.count() == 0:
            app.group.create(Group(name='Test'))
        groups = orm.get_group_list()
    with allure.step('Given a random contact from the list'):
        edit_contact = random.choice(contacts)
    with allure.step('Given a random group from the list'):
        del_group_from_contact = random.choice(groups)
    if len(orm.contacts_in_group(del_group_from_contact)) == 0:
        app.contact.add_contact_in_group_by_id(edit_contact.identifier, del_group_from_contact.identifier)
    with allure.step('When I delete contact %s in group %s from the list' % (edit_contact, del_group_from_contact)):
        app.contact.del_contact_from_group_by_id(edit_contact.identifier, del_group_from_contact.identifier)
    with allure.step('Then the edited contact will not be in the contact list of the selected group'):
        new_contacts = orm.get_contact_list()
        list_contacts_not_in_group = orm.contacts_not_in_group(del_group_from_contact)
        assert edit_contact in list_contacts_not_in_group
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
