import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.helpers import Helpers

class CheckoutPage:

    def __init__(self,driver):
        self.h = Helpers(driver)
        self.driver = driver
        self.CHECKOUT_TOTAL = (By.CSS_SELECTOR, "#orderModal #totalm")
        self.CHECKOUT_FORM_NAME = (By.CSS_SELECTOR, "#orderModal #name")
        self.CHECKOUT_FORM_COUNTRY = (By.CSS_SELECTOR, "#orderModal #country")
        self.CHECKOUT_FORM_CITY = (By.CSS_SELECTOR, "#orderModal #city")
        self.CHECKOUT_FORM_CARD = (By.CSS_SELECTOR, "#orderModal #card")
        self.CHECKOUT_FORM_MONTH = (By.CSS_SELECTOR, "#orderModal #month")
        self.CHECKOUT_FORM_YEAR = (By.CSS_SELECTOR, "#orderModal #year")
        self.CHECKOUT_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#orderModal button.btn.btn-primary")
        self.CHECKOUT_CONFIRMATION = (By.CSS_SELECTOR, "p.lead.text-muted")
        self.CHECKOUT_OK_BUTTON = (By.CSS_SELECTOR, "button.confirm.btn.btn-lg.btn-primary")

    def get_total_in_checkout(self):

        timeout = time.time() + 10  

        while time.time() < timeout:

            element = self.h.get_element(self.CHECKOUT_TOTAL)
            if len(element.text) > 0:
                break
        
        price_checkout_trimmed = element.text.replace("Total: ","")

        return price_checkout_trimmed

    def fill_checkout_form(self, test_data):
        
        self.h.send_keys_to_elem(self.CHECKOUT_FORM_NAME,test_data["name"])
        self.h.send_keys_to_elem(self.CHECKOUT_FORM_COUNTRY,test_data["country"])
        self.h.send_keys_to_elem(self.CHECKOUT_FORM_CITY,test_data["city"])
        self.h.send_keys_to_elem(self.CHECKOUT_FORM_CARD,test_data["card"])
        self.h.send_keys_to_elem(self.CHECKOUT_FORM_MONTH,test_data["month"])
        self.h.send_keys_to_elem(self.CHECKOUT_FORM_YEAR,test_data["year"])