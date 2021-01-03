from model.contact import Contact


def test_delete_first_contact(app):
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
                               home="13",
                               notes="Oleg is a good man"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # delete first element in the list
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
