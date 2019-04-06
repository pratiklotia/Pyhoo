# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Unsubscriber(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_unsubscriber(self):
        driver = self.driver
        driver.get("https://mail.yahoo.com/")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sign up'])[1]/following::span[1]").click()
        driver.find_element_by_id("login-username").click()
        driver.find_element_by_id("login-username").clear()
        driver.find_element_by_id("login-username").send_keys("pratiklotia@yahoo.in")
        driver.find_element_by_id("login-signin").click()
        driver.find_element_by_name("code").clear()
        driver.find_element_by_name("code").send_keys("KTQE")
        driver.find_element_by_name("verify").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Nikita'])[1]/following::span[4]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='Nikita'])[1]/following::span[4] | ]]
        driver.find_element_by_link_text("Click here").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Catch up on the most popular videos on Yahoo'])[1]/following::span[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Club Oxygen'])[1]/following::span[4]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='Club Oxygen'])[1]/following::span[4] | ]]
        driver.find_element_by_link_text("To Stop It Click Here").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Catch up on the most popular videos on Yahoo'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Kalyan Matrimony'])[1]/following::span[4]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='Kalyan Matrimony'])[1]/following::span[4] | ]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='View this email in your browser'])[1]/following::a[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Catch up on the most popular videos on Yahoo'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='A.O. Smith'])[1]/following::span[4]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='A.O. Smith'])[1]/following::span[4] | ]]
        driver.find_element_by_link_text("Unsubscribe me from this mailing list").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Catch up on the most popular videos on Yahoo'])[1]/following::span[2]").click()
    
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
