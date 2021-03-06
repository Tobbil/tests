import time
import unittest
import os
import sys
from PageObject import MainPage, CartPage, LogInPage, SignUpPage, ContactPage, CheckoutPage
from WebDriverSetup import WebDriverSetup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from PageObject.helpers import Helpers

class TestLogIn(WebDriverSetup):

    test_data = {"username":"MrTester","password":"test0TEST."}

    def test_login(self):

        driver = self.driver
        h = Helpers(driver)
        test_data = self.test_data
        main_page = MainPage.MainPage(driver)
        login_page = LogInPage.LogInPage(driver)
        driver.get("https://www.demoblaze.com/")
        h.click_element(main_page.LOG_IN)
        login_page.fill_username_and_password(test_data)
        time.sleep(1)
        h.click_element(login_page.LOGIN_BUTTON)
        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element(main_page.USERNAME_IN_MENU,"Welcome"))
        element = h.get_element(main_page.USERNAME_IN_MENU)
        self.assertEqual(element.text,f"Welcome {test_data['username']}")
        h.click_element(main_page.LOG_OUT)
        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element(main_page.LOG_IN,"Log in"))
        element = h.get_element(main_page.LOG_IN)
        self.assertEqual(element.text,"Log in")
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()