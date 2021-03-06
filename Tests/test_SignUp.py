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

class TestSignUp(WebDriverSetup):

    test_data = {"username":"MrTester","password":"test0TEST."}

    def test_sign_up(self):

        driver = self.driver
        h = Helpers(driver)
        test_data = self.test_data
        main_page = MainPage.MainPage(driver)
        signup_page = SignUpPage.SignUpPage(driver)
        driver.get("https://www.demoblaze.com/")
        h.click_element(main_page.SIGN_UP)
        signup_page.fill_username_and_password(test_data)
        time.sleep(1)
        h.click_element(signup_page.SIGN_UP_BUTTON)
        WebDriverWait(driver,10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(f"Alert message: {alert.text}")
        alert.accept()
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()