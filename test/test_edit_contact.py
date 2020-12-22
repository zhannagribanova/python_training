from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(firstname="Oleg",
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
                               home="133",
                               notes="Maksim is a good man"))
