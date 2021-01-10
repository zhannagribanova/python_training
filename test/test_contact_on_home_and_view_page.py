import re


def test_contact_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merge_emails_like_on_home_and_edit_page(contact_from_edit_page)
    assert contact_from_home_page.address_company == contact_from_edit_page.address_company
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.identifier == contact_from_edit_page.identifier


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.telephone_home == contact_from_edit_page.telephone_home
    assert contact_from_view_page.telephone_work == contact_from_edit_page.telephone_work
    assert contact_from_view_page.telephone_mobile == contact_from_edit_page.telephone_mobile
    assert contact_from_view_page.telephone_secondary == contact_from_edit_page.telephone_secondary


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.telephone_home, contact.telephone_mobile, contact.telephone_work,
                                        contact.telephone_secondary]))))


def merge_emails_like_on_home_and_edit_page(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None, [contact.email1, contact.email2, contact.email3]))

