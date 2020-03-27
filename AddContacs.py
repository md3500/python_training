# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AddContacs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_contacs(self):
        driver = self.driver
        driver.get("http://localhost/group.php")
        self.Login(driver, username="admin", password="secret")
        self.New_contact(driver)
        self.add_first_name(driver, first_name="Nichita")
        self.add_middle_name(driver, middlename="Nick")
        self.add_last_name(driver, last_name="Orlic")
        self.add_nickname(driver, nickname="md350")
        self.add_title(driver, title="Test")
        self.add_company_name(driver, company_name="Software Testing")
        self.add_address(driver, address="Russia")
        self.add_home_number(driver, home_number="7490000000")
        self.add_mobile_number(driver, mobile_number="7920000000")
        self.add_work_number(driver, work_number="7910000000")
        self.add_email(driver, email="pzvn95@gmail.com")
        self.add_homepage(driver, homepage="vk.com/nickmd")
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        driver.find_element_by_link_text("home page").click()
        driver.find_element_by_link_text("Logout").click()

    def add_homepage(self, driver, homepage):
        driver.find_element_by_name("homepage").click()
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys(homepage)

    def add_email(self, driver, email):
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(email)

    def add_work_number(self, driver, work_number):
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(work_number)

    def add_mobile_number(self, driver, mobile_number):
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(mobile_number)

    def add_home_number(self, driver, home_number):
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(home_number)

    def add_address(self, driver, address):
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(address)

    def add_company_name(self, driver, company_name):
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(company_name)

    def add_title(self, driver, title):
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(title)

    def add_nickname(self, driver, nickname):
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(nickname)

    def add_last_name(self, driver, last_name):
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(last_name)

    def add_middle_name(self, driver, middlename):
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(middlename)

    def add_first_name(self, driver, first_name):
        driver.find_element_by_name("firstname").send_keys(first_name)

    def New_contact(self, driver):
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()

    def Login(self, driver, username, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

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
