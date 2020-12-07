# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddAddressBookEntry(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_address_book_entry(self):
        driver = self.driver
        driver.get("http://localhost/addressbook")
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("Oleg")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("Ivan")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("Kolesnikov")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("olegkolesnikov")
        driver.find_element_by_name("photo").click()
        driver.find_element_by_name("photo").clear()
        driver.find_element_by_name("photo").send_keys("C:\\fakepath\\photo_2019-01-28_23-36-11.jpg")
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("Title")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("Apple")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("USA California")
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("13-13-13")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("89111111111")
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("2-12-12")
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys("123-123-123-123")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("test1@test.ru")
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys("test2@test.ru")
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys("test3@test.ru")
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys("https://test.ru")
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("1")
        driver.find_element_by_name("bday").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("January")
        driver.find_element_by_name("bmonth").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1990")
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text("1")
        driver.find_element_by_name("aday").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("January")
        driver.find_element_by_name("amonth").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("2030")
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("Russia, Saint-Petersburg")
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("13")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("Oleg is a good man")
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        driver.find_element_by_link_text("home page").click()
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
