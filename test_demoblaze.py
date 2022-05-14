import time
import unittest
import os
import sys
import page
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


class TestDemoblazeAddToCart(unittest.TestCase):

    test_data = {"name":"Mr Test","country":"Norway","city":"Tromsø",
                "card":"4376232127005830","month":"May","year":"2022"}

    def setUp(self):
        self.driver = webdriver.Chrome(os.path.join(sys.path[0], "chromedriver"))
        self.driver.get("https://www.demoblaze.com/")
        
    def test_add_to_cart(self):
        driver = self.driver
        test_data = self.test_data
        driver.implicitly_wait(10)
        main_page = page.MainPage(driver)
        main_page.click_menu_phones()
        element = main_page.test_price_in_list()
        self.assertEqual("$360",element.text)
        element = main_page.test_phone_name_in_list()
        self.assertEqual("Samsung galaxy s6",element.text)
        element = main_page.test_phone_name_in_list()
        element.click()
        element = main_page.test_price_in_item_page()
        price_add_to_cart_trimmed = element.text.replace(" *includes tax","")
        self.assertEqual("$360",price_add_to_cart_trimmed)
        element = main_page.test_phone_name_in_item_page()
        self.assertEqual("Samsung galaxy s6",element.text)
        element = main_page.test_description_in_item_page()
        self.assertNotEqual("",element.text)
        self.assertNotEqual(" ",element.text)
        element = main_page.test_add_to_cart_button()
        self.assertEqual("Add to cart",element.text)
        element.click()
        WebDriverWait(driver,10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        message = alert.text
        self.assertEqual("Product added",message)
        alert.accept()
        element = main_page.test_go_to_cart()
        element.click()
        self.assertTrue(main_page.test_cart_content())
        element = main_page.test_cart_total()
        self.assertIn(element.text,"$360")
        element = main_page.test_price_in_table()
        self.assertIn(element.text,"$360")
        element = main_page.test_phone_name_in_table()
        self.assertEqual("Samsung galaxy s6",element.text)
        # tu test dla delete

        # tu test dla delete
        element = main_page.test_place_order_button()
        self.assertEqual("Place Order",element.text)
        element.click()
        element = main_page.test_total_in_checkout()
        price_checkout_trimmed = element.text.replace("Total: ","")
        self.assertEqual(price_checkout_trimmed,"360")
        checkout_elements = main_page.test_fill_out_checkout_form()
        checkout_elements[0].send_keys(test_data["name"])
        checkout_elements[1].send_keys(test_data["country"])
        checkout_elements[2].send_keys(test_data["city"])
        checkout_elements[3].send_keys(test_data["card"])
        checkout_elements[4].send_keys(test_data["month"])
        checkout_elements[5].send_keys(test_data["year"])
        element = main_page.test_submit_purchase()
        element.click()
        # tu assert danych w alercie
        
        # tu assert danych w alercie
        element = main_page.test_OK_button_purchase()
        element.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()