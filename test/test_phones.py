import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.telephone_home == clear(contact_from_edit_page.telephone_home)
    assert contact_from_home_page.telephone_work == clear(contact_from_edit_page.telephone_work)
    assert contact_from_home_page.telephone_mobile == clear(contact_from_edit_page.telephone_mobile)
    assert contact_from_home_page.telephone_secondary == clear(contact_from_edit_page.telephone_secondary)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.telephone_home == contact_from_edit_page.telephone_home
    assert contact_from_view_page.telephone_work == contact_from_edit_page.telephone_work
    assert contact_from_view_page.telephone_mobile == contact_from_edit_page.telephone_mobile
    assert contact_from_view_page.telephone_secondary == contact_from_edit_page.telephone_secondary


def clear(s):
    return re.sub("[() -]", "", s)
