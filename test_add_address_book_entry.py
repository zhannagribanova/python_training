# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_address_book_entry(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Oleg", middlename="Ivan", lastname="Kolesnikov", nickname="olegkolesnikov",
                            photo="C:\\Users\\j.gribanova\\Pictures\\photo_2019-01-28_23-36-11.jpg", title="Title",
                            company="Apple", address_company="USA California", telephone_home="13-13-13",
                            telephone_mobile="89111111111", telephone_work="2-12-12", fax="123-123-123-123",
                            email1="test1@test.ru", email2="test2@test.ru", email3="test3@test.ru",
                            homepage="https://test.ru", bday="1", bmonth="January", byear="1990", aday="1",
                            amonth="January", ayear="2030", home_address="Russia, Saint-Petersburg", home="13",
                            notes="Oleg is a good man"))
    app.logout()
