from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_element_by_link_text("Last name")) > 0):
            wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_element_by_link_text("Last name")) > 0):
            wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_page()
        self.contact_data(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.edit_contact_by_index(0, new_contact_data)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.contact_data(new_contact_data)
        # submit edit contact
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        self.contact_data(new_contact_data)
        # submit edit contact
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def change_fild_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_the_date_fild_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).click()

    def contact_data(self, contact):
        # fill contact form, name input
        self.change_fild_value("firstname", contact.firstname)
        self.change_fild_value("middlename", contact.middlename)
        self.change_fild_value("lastname", contact.lastname)
        self.change_fild_value("nickname", contact.nickname)
        # photo upload
        self.change_fild_value("photo", contact.photo)
        # information about work
        self.change_fild_value("title", contact.title)
        self.change_fild_value("company", contact.company)
        self.change_fild_value("address", contact.address_company)
        # telephones
        self.change_fild_value("home", contact.telephone_home)
        self.change_fild_value("mobile", contact.telephone_mobile)
        self.change_fild_value("work", contact.telephone_work)
        self.change_fild_value("fax", contact.fax)
        # e-mails and homepage
        self.change_fild_value("email", contact.email1)
        self.change_fild_value("email2", contact.email2)
        self.change_fild_value("email3", contact.email3)
        self.change_fild_value("homepage", contact.homepage)
        # birthday
        self.change_the_date_fild_value("bday", contact.bday)
        self.change_the_date_fild_value("bmonth", contact.bmonth)
        self.change_fild_value("byear", contact.byear)
        # anniversary
        self.change_the_date_fild_value("aday", contact.aday)
        self.change_the_date_fild_value("amonth", contact.amonth)
        self.change_fild_value("ayear", contact.ayear)
        # address
        self.change_fild_value("address2", contact.home_address)
        self.change_fild_value("phone2", contact.telephone_secondary)
        # notes
        self.change_fild_value("notes", contact.notes)

    def open_add_new_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector('tr[name="entry"]'):
                firstname_text = element.find_element_by_css_selector("td:nth-child(3)").text
                lastname_text = element.find_element_by_css_selector("td:nth-child(2)").text
                identifier = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = element.find_element_by_css_selector("td:nth-child(6)").text
                all_email = element.find_element_by_css_selector("td:nth-child(5)").text
                address = element.find_element_by_css_selector("td:nth-child(4)").text
                self.contact_cache.append(Contact(firstname=firstname_text, lastname=lastname_text,
                                                  identifier=identifier, all_phones_from_home_page=all_phones,
                                                  all_email_from_home_page=all_email, address_company=address))
        return self.contact_cache

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").text
        return Contact(firstname=firstname, lastname=lastname, identifier=id, telephone_home=homephone,
                       telephone_work=workphone, telephone_mobile=mobilephone, telephone_secondary=secondaryphone,
                       email1=email1, email2=email2, email3=email3, address_company=address)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("(// img[@ alt='Edit'])["+str(index+1)+"]").click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//a[contains(@href, 'edit.php?id="+str(id)+"')]").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("(// img[@ alt='Details'])["+str(index+1)+"]").click()

    @staticmethod
    def search_in_text(search_text, text):
        search_result = re.search(search_text, text)
        if search_result is not None:
            return search_result.group(1)
        else:
            return ''
        # Тернарный оператор: return search_result.group(1) if search_result is not None else ''

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = self.search_in_text("H: (.*)", text)
        workphone = self.search_in_text("W: (.*)", text)
        mobilephone = self.search_in_text("M: (.*)", text)
        secondaryphone = self.search_in_text("P: (.*)", text)
        return Contact(telephone_home=homephone, telephone_work=workphone, telephone_mobile=mobilephone,
                       telephone_secondary=secondaryphone)

