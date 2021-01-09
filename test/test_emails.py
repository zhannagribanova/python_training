
def test_emails_on_home_page(app):
    email_from_home_page = app.contact.get_contact_list()[0]
    email_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert email_from_home_page.all_email_from_home_page == merge_emails_like_on_home_and_edit_page(email_from_edit_page)


def merge_emails_like_on_home_and_edit_page(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None, [contact.email1, contact.email2, contact.email3]))
