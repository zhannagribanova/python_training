# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddAddressBookEntry(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_address_book_entry(self):
        wd = self.wd
        wd.get("http://localhost/addressbook")

        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Oleg")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Ivan")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Kolesnikov")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("olegkolesnikov")
        wd.find_element_by_name("photo").clear()
        wd.find_element_by_name("photo").send_keys("C:\\Users\\j.gribanova\\Pictures\\photo_2019-01-28_23-36-11.jpg")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("Title")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("Apple")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("USA California")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("13-13-13")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("89111111111")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("2-12-12")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("123-123-123-123")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("test1@test.ru")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("test2@test.ru")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("test3@test.ru")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("https://test.ru")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("1")
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("January")
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2030")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("Russia, Saint-Petersburg")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("13")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("Oleg is a good man")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()
        wd.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
